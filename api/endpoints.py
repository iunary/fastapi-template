from fastapi import APIRouter
from api import health

routers = APIRouter()
routers.include_router(health.routers, tags=["health"])
