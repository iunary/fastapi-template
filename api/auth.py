from fastapi import APIRouter

routers = APIRouter(prefix="/auth")


@routers.post("/login")
async def login():
    pass


@routers.post("/register")
async def register():
    pass


@routers.post("/password/reset")
async def password_reset():
    pass


@routers.post("/password/update")
async def password_update():
    pass
