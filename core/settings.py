from typing import List

from pydantic import BaseSettings


class Settings(BaseSettings):
    DEBUG: bool = False
    SERVICE_NAME: str = "fastapi"
    SERVICE_VERSION = "1.0.0"
    SERVICE_DESCRIPTION = ""
    BATABASE_URL: str = ""
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000
    JWT_SECRET: str = "202a680db93796157db4d5a421820fad"
    JWT_ALGORITHM: str = "HS256"
    JWT_TOKEN_EXPIRE_MINUTES: int = 20
    ALLOWD_HOSTS: List[str] = ["*"]


settings: Settings = Settings()
