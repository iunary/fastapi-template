from datetime import datetime, timedelta
from typing import Optional

from jose import JWTError, jwt

from core.settings import settings

from core.auth.schemas import Claims


def create_access_token(data: Claims) -> str:
    claims = {
        "sub": data.email,
        "exp": datetime.utcnow() + timedelta(minutes=settings.JWT_TOKEN_EXPIRE_MINUTES),
    }

    return jwt.encode(
        claims=claims, key=settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM
    )


def verify_token(token: str) -> Optional[Claims]:
    try:
        payload = jwt.decode(
            token=token, key=settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM]
        )
        email: str = payload.get("sub", None)
        if email is None:
            return None
        return Claims(email=email)
    except JWTError:
        return None
