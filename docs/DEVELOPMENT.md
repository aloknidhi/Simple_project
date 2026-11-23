# Development Guide

## Personal AI Brain - Developer Documentation

This guide covers setting up the development environment, project structure, coding standards, and contribution workflow.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Project Setup](#project-setup)
3. [Project Structure](#project-structure)
4. [Running the Application](#running-the-application)
5. [Environment Variables](#environment-variables)
6. [Database Migrations](#database-migrations)
7. [API Development](#api-development)
8. [Frontend Development](#frontend-development)
9. [Testing](#testing)
10. [Code Style Guidelines](#code-style-guidelines)
11. [Git Workflow](#git-workflow)
12. [Deployment](#deployment)

---

## Prerequisites

### System Requirements

- **Operating System:** Linux (Ubuntu 22.04+), macOS 13+, or Windows 11+ with WSL2
- **Docker:** 24.0+
- **Docker Compose:** 2.20+
- **Node.js:** 18.x or 20.x
- **Python:** 3.12.x

### Required Tools

```bash
# Check versions
node --version      # Should be 18.x or 20.x
python --version    # Should be 3.12.x
docker --version    # Should be 24.x
docker compose version  # Should be 2.x
```

### Install Tools (if needed)

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install -y curl git docker.io docker-compose-plugin

# Node.js
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt install -y nodejs

# Python
sudo apt install -y python3.12 python3.12-venv python3-pip

# Verify
node -v
python3 --version
docker --version
docker compose version
```

---

## Project Setup

### 1. Clone the Repository

```bash
git clone https://github.com/aloknidhi/Simple_project.git
cd Simple_project
```

### 2. Create .env File

```bash
cp .env.example .env
```

Edit `.env` with your actual values:
- `OPENAI_API_KEY`: Get from https://platform.openai.com/api-keys
- `SECRET_KEY`: Generate with `python -c "import secrets; print(secrets.token_urlsafe(32))"`

### 3. Build Docker Containers

```bash
docker compose build
```

### 4. Run Migrations

```bash
# Start database first
docker compose up -d db redis

# Run migrations
docker compose exec backend alembic upgrade head

# Or run manually
docker compose exec backend python -c "
from app.database import engine, Base
from app.models import *
import asyncio
asyncio.run(Base.metadata.create_all(bind=engine))
"
```

### 5. Start All Services

```bash
docker compose up
```

The application should now be accessible:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- Database: localhost:5432
- pgAdmin: http://localhost:5050

---

## Project Structure

```
personal-ai-brain/
│
├── .github/
│   └── workflows/
│       └── ci.yml              # CI/CD pipeline
├── .env.example               # Environment template
├── docker-compose.yml         # Docker orchestration
├── daily/                     # Daily progress logs
│   ├── Day-1-Setup.md
│   ├── Day-2-Database.md
│   └── ...
├── docs/
│   ├── API.md                # API documentation
│   ├── ARCHITECTURE.md       # System architecture
│   ├── DEVELOPMENT.md        # This file
│   └── SRS.md                # Requirements spec
├── database/
│   ├── init.sql              # Initial schema
│   └── migrations/           # Alembic migrations
│       ├── env.py
│       ├── README
│       └── versions/
├── frontend/
│   ├── Dockerfile
│   ├── nginx.conf
│   ├── package.json
│   ├── package-lock.json
│   ├── public/
│   ├── src/
│   │   ├── api/              # API client
│   │   ├── components/       # Reusable components
│   │   ├── hooks/            # Custom hooks
│   │   ├── pages/            # Route pages
│   │   ├── routes/           # Route definitions
│   │   ├── services/         # API services
│   │   ├── styles/           # Global styles
│   │   ├── types/            # TypeScript types
│   │   ├── utils/            # Utility functions
│   │   ├── App.tsx
│   │   └── main.tsx
│   └── vite.config.ts
├── backend/
│   ├── alembic.ini
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py           # Application entry point
│   │   ├── api/              # API routes
│   │   ├── core/             # Core configuration
│   │   ├── db/               # Database setup
│   │   ├── models/           # SQLAlchemy models
│   │   ├── schemas/          # Pydantic schemas
│   │   ├── services/         # Business logic
│   │   ├── ai/               # AI integration
│   │   ├── security/         # Auth & security
│   │   └── utils/            # Utility functions
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── test_auth.py
│   │   ├── test_sources.py
│   │   └── test_knowledge.py
│   ├── Dockerfile
│   └── requirements.txt
└── storage/
    └── .gitkeep
```

---

## Running the Application

### Start All Services

```bash
docker compose up
```

### Start Specific Services

```bash
# Database only
docker compose up -d db redis

# Frontend only (requires db)
docker compose up -d db redis
docker compose up frontend

# Backend only (requires db)
docker compose up -d db redis
docker compose up backend

# Production-like build
docker compose -f docker-compose.yml -f docker-compose.prod.yml up
```

### Stop All Services

```bash
docker compose down
```

### View Logs

```bash
# All services
docker compose logs -f

# Specific service
docker compose logs -f backend
docker compose logs -f frontend
```

### Execute Commands in Container

```bash
# Run Python in backend
docker compose exec backend python -c "print('Hello')"

# Run tests in backend
docker compose exec backend pytest

# Open bash in backend
docker compose exec backend bash
```

---

## Environment Variables

### Backend Environment Variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `DATABASE_URL` | Yes | - | PostgreSQL connection string |
| `SECRET_KEY` | Yes | - | JWT secret key |
| `OPENAI_API_KEY` | Yes | - | OpenAI API key |
| `BACKEND_HOST` | No | `0.0.0.0` | Backend server host |
| `BACKEND_PORT` | No | `8000` | Backend server port |
| `DEBUG` | No | `false` | Enable debug mode |
| `LOG_LEVEL` | No | `INFO` | Logging level |
| `CORS_ORIGINS` | No | `*` | Allowed CORS origins |
| `REDIS_URL` | No | `redis://localhost:6379/0` | Redis connection |

### Frontend Environment Variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `VITE_API_URL` | Yes | - | Backend API base URL |
| `VITE_APP_NAME` | No | `Personal AI Brain` | Application name |
| `VITE_SUPPORT_EMAIL` | No | - | Support email |

### Example .env File

```bash
# Backend
DATABASE_URL=postgresql://ai_user:secure_password@db:5432/personal_ai_brain
SECRET_KEY=change-this-in-production-use-secrets-token_urlsafe-32
OPENAI_API_KEY=sk-your-openai-key
BACKEND_HOST=0.0.0.0
BACKEND_PORT=8000
DEBUG=true
LOG_LEVEL=INFO
CORS_ORIGINS=http://localhost:3000,http://localhost:8000

# Frontend
VITE_API_URL=http://localhost:8000/api/v1
VITE_APP_NAME=Personal AI Brain
VITE_SUPPORT_EMAIL=support@ai-brain.local

# Redis
REDIS_URL=redis://redis:6379/0
```

---

## Database Migrations

### Create Migration

```bash
# Generate migration from model changes
docker compose exec backend alembic revision --autogenerate -m "Add new feature"

# Manual migration
docker compose exec backend alembic revision -m "Custom migration"
```

### Apply Migrations

```bash
# Apply pending migrations
docker compose exec backend alembic upgrade head

# Upgrade to specific version
docker compose exec backend alembic upgrade -1

# Show current version
docker compose exec backend alembic current
```

### Rollback Migration

```bash
# Rollback last migration
docker compose exec backend alembic downgrade -1

# Rollback to specific version
docker compose exec backend alembic downgrade base
```

### Migration Directory Structure

```
database/migrations/
├── env.py              # Alembic environment
├── README              # Migration documentation
└── versions/
    ├── 20241123000001_initial.py
    └── 20241123000002_add_ai_models.py
```

---

## API Development

### Adding a New Endpoint

1. **Create Schema** (`backend/app/schemas/`)
```python
from pydantic import BaseModel

class ExampleCreate(BaseModel):
    name: str
    description: str | None = None
```

2. **Create Model** (`backend/app/models/`)
```python
from sqlalchemy import Column, String, Text
from app.db.base_class import Base

class Example(Base):
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
```

3. **Add Endpoint** (`backend/app/api/endpoints/`)
```python
from fastapi import APIRouter

router = APIRouter()

@router.post("/")
async def create_example(payload: schemas.ExampleCreate):
    # Implementation
    return {"id": 1, **payload.model_dump()}
```

4. **Register Router** (`backend/app/api/api.py`)
```python
from .endpoints import example

api_router.include_router(example.router, prefix="/examples", tags=["examples"])
```

### Testing Endpoints

```bash
# Run API tests
docker compose exec backend pytest tests/test_api.py -v

# Test specific endpoint
curl -X POST http://localhost:8000/api/v1/examples \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -d '{"name": "Test"}'
```

---

## Frontend Development

### Component Structure

```tsx
// components/Button.tsx
import { FC } from 'react';

interface ButtonProps {
  onClick: () => void;
  children: React.ReactNode;
  variant?: 'primary' | 'secondary';
  disabled?: boolean;
}

export const Button: FC<ButtonProps> = ({ onClick, children, variant = 'primary', disabled = false }) => {
  return (
    <button 
      onClick={onClick}
      className={`btn btn-${variant} ${disabled ? 'disabled' : ''}`}
      disabled={disabled}
    >
      {children}
    </button>
  );
};
```

### Hook Structure

```tsx
// hooks/useApi.ts
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import { apiClient } from '@/api/client';

export const useExamples = () => {
  return useQuery(['examples'], () => apiClient.getExamples());
};

export const useCreateExample = () => {
  const queryClient = useQueryClient();
  return useMutation(apiClient.createExample, {
    onSuccess: () => queryClient.invalidateQueries(['examples'])
  });
};
```

### Run Frontend Development Server

```bash
# Using Docker
docker compose up -d frontend

# Or locally
cd frontend
npm install
npm run dev
```

The frontend will be available at http://localhost:3000 with hot-reload enabled.

---

## Testing

### Backend Testing

```bash
# Run all tests
docker compose exec backend pytest

# Run with coverage
docker compose exec backend pytest --cov=app --cov-report=html

# Run specific test file
docker compose exec backend pytest tests/test_auth.py -v

# Run with debug
docker compose exec backend pytest -v --pdb
```

### Frontend Testing

```bash
cd frontend

# Run tests
npm test

# Run with coverage
npm test -- --coverage

# Run in watch mode
npm test -- --watch
```

### Test Structure

```
tests/
├── conftest.py          # Pytest configuration
├── test_auth.py       # Authentication tests
├── test_auth.py       # Source tests
└── test_knowledge.py  # Knowledge tests
```

---

## Code Style Guidelines

### Python (Backend)

Follow PEP 8 with these additions:

```python
# Use type hints everywhere
def calculate_mastery(user_id: str, topic_id: str) -> float:
    ...

# Use Pydantic for validation
class TopicUpdate(BaseModel):
    mastery_level: Literal["not_started", "learning", "practiced", "mastered"]
    confidence_score: Annotated[float, Field(ge=0, le=1)]

# Use dependency injection
router = APIRouter()

@router.get("/topics/{topic_id}")
async def get_topic(
    topic_id: str,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    ...
```

### TypeScript (Frontend)

```tsx
// Use interfaces for props
interface TopicCardProps {
  topic: ITopic;
  onUpdate: (topic: ITopic) => void;
}

// Use proper typing
const [topics, setTopics] = useState<ITopic[]>([]);

// Async/await with error handling
const fetchTopics = async () => {
  try {
    const data = await api.getTopics();
    setTopics(data);
  } catch (error) {
    console.error('Failed to fetch topics:', error);
  }
};
```

### Git Hooks

Install pre-commit hooks:

```bash
pip install pre-commit
pre-commit install
```

Pre-commit configuration in `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.1.10
    hooks:
      - id: ruff
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.8.0
    hooks:
      - id: mypy
```

---

## Git Workflow

### Branch Naming Convention

```
feature/add-chatgpt-import    # New feature
fix/correct-timer-bug         # Bug fix
hotfix/urgent-security-patch  # Urgent fix
release/v1.0.0                # Release
docs/update-api-docs          # Documentation
```

### Development Workflow

```bash
# 1. Create feature branch
git checkout -b feature/add-chatgpt-import

# 2. Make changes
git add .
git commit -m "feat: add chatgpt import functionality

- Implement ZIP file parser
- Add conversation extraction
- Include deduplication logic

Closes #42"

# 3. Push changes
git push origin feature/add-chatgpt-import

# 4. Create Pull Request via GitHub UI
```

### Commit Message Format

Follow conventional commits:

```
<type>(<scope>): <subject>

<body>

<footer>
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `style`: Code formatting
- `refactor`: Code refactoring
- `test`: Adding tests
- `chore`: Maintenance tasks

Example:
```
feat(knowledge): add topic mastery tracking

- Add mastery level enum
- Implement confidence scoring
- Add revision scheduling

Resolves #15
```

---

## Deployment

### Production Deployment

1. **Build Docker Images**

```bash
docker compose build
```

2. **Run on Production Server**

```bash
# Pull latest code
git pull origin main

# Build and start
docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d
```

3. **Database Migrations**

```bash
docker compose exec backend alembic upgrade head
```

4. **Verify Deployment**

```bash
# Check container status
docker compose ps

# Check logs
docker compose logs -f

# Test API endpoint
curl https://api.personalaibrain.com/health
```

### Environment Variables for Production

Use a `.env.production` file:

```bash
DEBUG=false
LOG_LEVEL=WARNING
DATABASE_URL=postgresql://user:pass@prod-db:5432/ai_brain
CORS_ORIGINS=https://app.personalaibrain.com
```

### Backup and Restore

```bash
# Backup database
docker compose exec db pg_dump -U ai_user personal_ai_brain > backup.sql

# Restore database
docker compose exec db psql -U ai_user personal_ai_brain < backup.sql
```

---

## Useful Commands

```bash
# View running containers
docker compose ps

# View container logs
docker compose logs [service]

# Execute command in container
docker compose exec [service] bash

# Rebuild container
docker compose build [service]

# Clean up unused containers
docker compose down --remove-orphans

# Restart services
docker compose restart

# Start services in background
docker compose up -d
```

---

## Troubleshooting

### Port Already in Use

```bash
# Find process using port
lsof -i :3000

# Kill process
kill -9 <PID>
```

### Database Connection Failed

```bash
# Check if database is running
docker compose ps db

# Check database logs
docker compose logs db

# Try connecting
docker compose exec db psql -U ai_user -d personal_ai_brain -c "SELECT 1;"
```

### API Returns 500 Errors

```bash
# Check backend logs
docker compose logs backend -f

# Check if OpenAI API key is valid
docker compose exec backend python -c "
import openai
openai.api_key = '$OPENAI_API_KEY'
print(openai.models.list())
"
```

### CORS Errors

Ensure `CORS_ORIGINS` in `.env` includes your frontend URL:
```bash
CORS_ORIGINS=http://localhost:3000,http://localhost:8000
```

---

## Getting Help

- **Documentation:** Check `/docs` directory
- **Issues:** Create GitHub issue
- **Discussions:** Use GitHub Discussions
- **Pull Requests:** Follow contribution guidelines

---

## License

This project is licensed under the MIT License.