# 🔗 TinyURL - Minimal URL Shortener with FastAPI

A lightweight URL shortener built with **FastAPI**, **PostgreSQL**, **Redis**, and **Docker**. This service allows you to shorten long URLs and redirect using a short code.

---

## 🚀 Features

- Shorten long URLs with a short, unique code
- Redirect from short URL to the original
- Fast lookups using Redis cache
- Persistent storage using PostgreSQL
- Scalable via Docker + Docker Compose

---

## 📁 Project Structure

```
.
├── cache.py
├── database.py
├── docker-compose.yml
├── Dockerfile
├── main.py
├── models.py
├── requirements.txt
├── schemas.py
├── utils.py
├── .env
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/tinyurl-fastapi.git
cd tinyurl-fastapi
```

### 2. Create a `.env` File

```env
DATABASE_URL=postgresql://postgres:postgres@db:5432/tinyurl
REDIS_URL=redis://redis
```

### 3. Start the Service

```bash
docker-compose up --build
```

### 4. Access the API

Open your browser to:  
📍 http://localhost:8000/docs — Swagger UI to test shortening and redirection

---

## 🎯 API Endpoints

### 🔹 POST `/shorten`
Shortens a long URL

**Request**:
```json
{
  "long_url": "https://example.com"
}
```

**Response**:
```json
{
  "short_url": "http://localhost:8000/abc123"
}
```

---

### 🔹 GET `/{short_code}`
Redirects to the original long URL

---

## 📦 Tech Stack

- **Framework**: FastAPI
- **Database**: PostgreSQL
- **Cache**: Redis
- **Deployment**: Docker + Docker Compose

---

## 🧪 Testing Locally

After running `docker-compose up`, use:

- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- Or cURL/Postman to hit endpoints directly

---

## 📜 License

MIT License
