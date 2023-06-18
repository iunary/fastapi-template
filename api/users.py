from fastapi import APIRouter, Depends, HTTPException, status

from core.auth import get_current_user
from models.user import User
from schemas.user import UserProfileResponse

routers = APIRouter(prefix="/users")


@routers.get("/me", response_model=UserProfileResponse)
async def profile(
    current_user: User = Depends(get_current_user),
):
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="user not found"
        )
    return current_user
