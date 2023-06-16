from pydantic import BaseModel, EmailStr


class Claims(BaseModel):
    email: EmailStr


class Token(BaseModel):
    access_token: str
    token_type: str
