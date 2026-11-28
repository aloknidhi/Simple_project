# Simple Project

A simple tracker application to learn the fundamentals of Python and AI/ML concepts.

## Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Python 3.12 + FastAPI |
| Frontend | React + TypeScript + Tailwind CSS (Vite) |
| Database | PostgreSQL 15 + pgvector |
| Cache | Redis |
| Auth | JWT (OAuth2) |
| Deployment | Docker + Docker Compose |

## Project Structure

```
Simple_project/
├── backend/        # FastAPI application
├── frontend/       # React + Vite frontend
├── database/       # SQL schema and migrations
├── docs/           # Documentation
├── docker-compose.yml
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.12+
- Node.js 18+
- Docker & Docker Compose

### Run with Docker (recommended)

```bash
git clone https://github.com/aloknidhi/Simple_project.git
cd Simple_project

cp backend/.env.example backend/.env
# edit backend/.env with your settings

docker-compose up
```

Services:

- Backend API: http://localhost:8000
- Frontend: http://localhost:3000
- Interactive API docs: http://localhost:8000/docs
- pgAdmin: http://localhost:5050

### Run backend locally

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Run frontend locally

```bash
cd frontend
npm install
npm run dev
```

## Core API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /healthz | Health check |
| POST | /api/v1/auth/register | Register a new user |
| POST | /api/v1/auth/login | Login and receive a JWT token |
| GET | /api/v1/auth/me | Get current user profile |

## License

MIT
