from fastapi import APIRouter, status
from fastapi.responses import Response, PlainTextResponse

routers = APIRouter()


@routers.get(
    "/health",
    response_model=str,
    description="health check",
    name="health",
    response_class=PlainTextResponse,
)
async def health() -> Response:
    return Response(
        content="OK",
        status_code=status.HTTP_200_OK,
        headers={"content-Type": "text/plain"},
    )
