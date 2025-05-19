from fastapi import FastAPI, HTTPException, Depends, Request
from sqlalchemy.orm import Session
import models, schemas, utils, cache, database
from fastapi.responses import RedirectResponse
from starlette.status import HTTP_404_NOT_FOUND
import os
from dotenv import load_dotenv

load_dotenv()
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

@app.post("/shorten", response_model=schemas.URLResponse)
def shorten_url(request: schemas.URLRequest, db: Session = Depends(database.SessionLocal)):
    existing = db.query(models.URL).filter(models.URL.long_url == request.long_url).first()
    if existing:
        return {"short_url": f"http://localhost:8000/{existing.short_code}"}
    
    while True:
        short_code = utils.generate_short_code()
        if not db.query(models.URL).filter_by(short_code=short_code).first():
            break
    url = models.URL(short_code=short_code, long_url=request.long_url)
    db.add(url)
    db.commit()
    db.refresh(url)
    cache.redis_client.set(short_code, request.long_url)
    return {"short_url": f"http://localhost:8000/{short_code}"}


@app.get("/{short_code}")
def redirect(short_code: str, request: Request, db: Session = Depends(database.SessionLocal)):
    long_url = cache.redis_client.get(short_code)
    if not long_url:
        db_url = db.query(models.URL).filter_by(short_code=short_code).first()
        if not db_url:
            raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="URL not found")
        long_url = db_url.long_url
        cache.redis_client.set(short_code, long_url)


    db.commit()

    return RedirectResponse(long_url)