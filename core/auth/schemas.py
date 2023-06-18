from pydantic import BaseModel, EmailStr


class Claims(BaseModel):
    email: EmailStr


class Token(BaseModel):
    access_token: str
    token_type: str


class RegisterRequest(BaseModel):
    email: EmailStr
    password: str
    confirm_password: str
