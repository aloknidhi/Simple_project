"""Application configuration loaded from environment variables."""

from typing import List

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # Database
    DATABASE_URL: str
    DATABASE_POOL_SIZE: int = 20
    DATABASE_MAX_OVERFLOW: int = 30

    # Redis
    REDIS_URL: str = "redis://localhost:6379/0"

    # Security
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    # OpenAI
    OPENAI_API_KEY: str | None = None
    OPENAI_MODEL: str = "gpt-4"
    OPENAI_EMBEDDING_MODEL: str = "text-embedding-3-large"

    # Server
    BACKEND_HOST: str = "0.0.0.0"
    BACKEND_PORT: int = 8000
    DEBUG: bool = True
    LOG_LEVEL: str = "INFO"

    # CORS
    CORS_ORIGINS: str = "http://localhost:3000,http://localhost:8000"

    # Frontend
    VITE_API_URL: str = "http://localhost:8000/api/v1"

    # Rate limiting
    RATE_LIMIT_REQUESTS: int = 100
    RATE_LIMIT_WINDOW: int = 60

    # File storage
    UPLOAD_DIR: str = "./storage/uploads"
    MAX_FILE_SIZE: int = 10485760

    @property
    def database_url_async(self) -> str:
        """Return the SQLAlchemy async variant of DATABASE_URL."""
        return self.DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://")

    @property
    def cors_origins_list(self) -> List[str]:
        return [origin.strip() for origin in self.CORS_ORIGINS.split(",") if origin.strip()]


settings = Settings()
