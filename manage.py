import typer
import uvicorn

# from app.app import app
from core.settings import settings

cmd = typer.Typer(no_args_is_help=True)


@cmd.command(name="run")
def run():
    """run application"""
    uvicorn.run(
        app="app.main:app", reload=True, port=settings.APP_PORT, host=settings.APP_HOST
    )


@cmd.command(name="migrate")
def migrate():
    pass


@cmd.command(name="createuser")
def createuser():
    pass


if __name__ == "__main__":
    cmd()
