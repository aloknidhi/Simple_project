"""One-time database seeding helpers (kept empty for Day 2 scaffold)."""

from app.db.session import init_db


async def seed() -> None:
    """Seed default data. No-op until Day 3+ introduces seed data."""
    await init_db()
