from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from database import Base 

class URL(Base):
    __tablename__ = "urls"
    id = Column(Integer,primary_key=True, index=True)
    short_code = Column(String(10), unique=True, index=True)
    long_url = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

