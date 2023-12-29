"""Main."""
__all__: list[str] = []

from litestar import Litestar
from uvicorn import run

from incrementum_api import settings
from incrementum_api.routers import create_incrementa_router


def create_app() -> Litestar:
    return Litestar(
        route_handlers=[create_incrementa_router()],
        debug=settings.app.DEBUG,
    )


app = create_app()

if __name__ == "__main__":
    run(
        app,
        host=settings.server.HOST,
        log_level=settings.server.LOG_LEVEL,
        port=settings.server.PORT,
        reload=settings.server.RELOAD,
        timeout_keep_alive=settings.server.KEEPALIVE,
    )
