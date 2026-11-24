"""Application entry point for the Personal AI Brain backend."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.api.v1.api import api_router
from app.db.session import init_db

app = FastAPI(
    title="Personal AI Brain",
    description="AI-powered personal knowledge and productivity management system",
    version="0.2.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api/v1")


@app.on_event("startup")
async def on_startup() -> None:
    """Initialize database tables on startup."""
    await init_db()


@app.get("/", tags=["health"])
def root() -> dict:
    return {
        "service": "personal-ai-brain",
        "version": "0.2.0",
        "status": "running",
    }


@app.get("/healthz", tags=["health"])
def health() -> dict:
    return {"status": "ok"}
