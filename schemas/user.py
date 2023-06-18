from pydantic import BaseModel, EmailStr, Field, root_validator


class UserProfileResponse(BaseModel):
    email: EmailStr
    is_active: bool

    class Config:
        orm_mode = True


class CreateUserRequest(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8)
    confirm_password: str = Field(..., min_length=8)

    @root_validator()
    def verify_password_match(cls, values):
        password = values.get("password")
        password_confirm = values.get("password_confirm")
        if password != password_confirm:
            raise ValueError("password didn't match")
        return values


class CreateUserResponse(BaseModel):
    email: EmailStr

    class Config:
        orm_mode = True
