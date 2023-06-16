from passlib.hash import bcrypt
from sqlalchemy import BigInteger, Boolean, Column, String

from core.db.mixins import TimestampMixin
from core.db.models import Base


class User(TimestampMixin, Base):
    __tablename__ = "users"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    email = Column(String(256), nullable=True, unique=True)
    password = Column(String(256), nullable=False)
    is_active = Column(Boolean, default=True)

    def hash_password(self):
        self.password = bcrypt.hash(self.password)

    def verify_password(self, plain_passord: str) -> bool:
        return bcrypt.verify(plain_passord, self.hash_password)
