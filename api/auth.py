from fastapi import APIRouter, Depends, HTTPException, status

from core.auth.jwt import BEARER, create_access_token
from core.auth.schemas import Claims, LoginRequest, Token
from models.user import User
from services.user import UserService

routers = APIRouter(prefix="/auth")


@routers.post("/login", response_model=Token)
async def login(data: LoginRequest, user_service: UserService = Depends()):
    user: User = await user_service.get_user_by_email(email=data.email)
    if not user or not user.verify_password(data.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="bad request"
        )
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="please activate your account"
        )

    # create the token
    claims: Claims = Claims(email=user.email)
    access_token = create_access_token(claims)
    return Token(access_token=access_token, token_type=BEARER)


@routers.post("/register")
async def register():
    pass


@routers.post("/password/reset")
async def password_reset():
    pass


@routers.post("/password/update")
async def password_update():
    pass
