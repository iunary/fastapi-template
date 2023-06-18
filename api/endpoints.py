from fastapi import APIRouter
from api import health, auth

routers = APIRouter()
routers.include_router(health.routers, tags=["health"])
routers.include_router(auth.routers, tags=["auth"])
