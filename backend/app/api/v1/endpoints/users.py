"""User endpoints."""

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_current_active_user, get_db
from app.models.user import User
from app.schemas.user import UserOut

router = APIRouter()


@router.get("/me", response_model=UserOut, tags=["users"])
async def read_users_me(current_user: User = Depends(get_current_active_user)) -> UserOut:
    return current_user
