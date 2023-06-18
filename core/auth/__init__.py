from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from core.auth.jwt import verify_token
from core.settings import settings
from models.user import User
from services.user import UserService

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=settings.AUTH_URL)


async def get_current_user(
    token: str = Depends(oauth2_scheme), user_service: UserService = Depends()
) -> User:
    claims = verify_token(token)
    if not claims:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="invalid token"
        )
    user = await user_service.get_user_by_email(claims.email)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="invalid token"
        )
    return user
