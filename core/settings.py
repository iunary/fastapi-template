from typing import List

from pydantic import BaseSettings


class Settings(BaseSettings):
    DEBUG: bool = False
    SERVICE_NAME: str = "fastapi"
    SERVICE_VERSION = "1.0.0"
    SERVICE_DESCRIPTION = ""
    BATABASE_URL: str = (
        "postgresql+psycopg2://postgres:nix@localhost:5432/hub?sslmode=disable"
    )
    APP_HOST: str = "0.0.0.0"  # nosec
    APP_PORT: int = 8000
    JWT_SECRET: str = "202a680db93796157db4d5a421820fad"
    JWT_ALGORITHM: str = "HS256"
    JWT_TOKEN_EXPIRE_MINUTES: int = 20
    ALLOWD_HOSTS: List[str] = ["*"]
    AUTH_URL: str = "/api/v1/auth/login"


settings: Settings = Settings()
