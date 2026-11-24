# Day 2: Backend & Frontend scaffolding

Completed on November 23, 2024 (Foundation phase - Day 2/7).

## Backend (`/backend`)
- `backend/Dockerfile` - Python 3.12 runtime, uvicorn entrypoint
- `backend/requirements.txt` - FastAPI, SQLAlchemy (async), alembic, python-jose, passlib, python-dotenv
- `backend/app/main.py` - FastAPI app, CORS, health endpoints
- `backend/app/core/config.py` - pydantic-settings configuration
- `backend/app/db/` - async SQLAlchemy engine, session dependency, Base
- `backend/app/models/user.py` - User ORM model matching `database/init.sql`
- `backend/app/schemas/` - UserCreate/UserOut, Token/TokenData
- `backend/app/services/user_service.py` - CRUD for users (bcrypt passwords)
- `backend/app/security/` - password hashing (passlib), JWT create/decode
- `backend/app/api/` - deps (get_current_user), v1 router, auth + users endpoints

## Frontend (`/frontend`)
- `frontend/Dockerfile` - Node 20 runtime
- `frontend/package.json` - React 18 + TypeScript + Vite + Tailwind CSS
- `frontend/vite.config.ts` - Vite dev server on port 3000, /api proxy to backend
- `frontend/src/App.tsx` - dashboard shell calling /api/healthz
- `frontend/src/main.tsx`, `index.css`, `tsconfig.json`, `tailwind.config.js`, `postcss.config.js`, `index.html`

## Verification
- Backend Python files compile cleanly (py_compile)
- package.json is valid JSON
- Dockerfiles present for both services (referenced by docker-compose.yml)

## Commits
Pushed to `main` as a single commit: "feat: add Day 2 backend and frontend scaffolding"
