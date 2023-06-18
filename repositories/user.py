from fastapi import Depends
from sqlalchemy.orm import Session

from core.db import get_database
from models.user import User


class UserRespository:
    def __init__(self, session: Session = Depends(get_database)) -> None:
        self.session = session

    def get_user_by_email(self, email: str) -> User:
        return self.session.query(User).filter(User.email == email).first()
