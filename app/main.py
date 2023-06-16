from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.settings import settings

app = FastAPI(
    title=settings.SERVICE_NAME,
    description=settings.SERVICE_DESCRIPTION,
    version=settings.SERVICE_VERSION,
    docs_url="/",
    debug=settings.DEBUG,
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWD_HOSTS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# register routes
