from typing import Optional

from fastapi import Depends, HTTPException, Request, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from core.auth.jwt import verify_token
from services.user import UserService


class AuthBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super().__init__(auto_error=auto_error)

    async def __call__(self, request: Request, user_service: UserService = Depends()):
        credentials: Optional[HTTPAuthorizationCredentials] = await super().__call__(
            request
        )
        if credentials and not credentials.scheme.lower() == "bearer":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="invalid authorization schema",
            )
        elif not credentials:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="invalid authorization code",
            )

        claims = verify_token(credentials.credentials)
        if not claims:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="invalid authorization token",
            )
        # get the user and check if its account is active
        user = await user_service.get_user_by_email(email=claims.email)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="invalid authorization token",
            )
        if not user.is_active:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="please confirm your account",
            )

        request.state.user = user.email
        return user
