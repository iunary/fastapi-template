from fastapi import APIRouter

from api import auth, health, users

routers = APIRouter()
routers.include_router(health.routers, tags=["health"])
routers.include_router(auth.routers, tags=["auth"])
routers.include_router(users.routers, tags=["users"])
