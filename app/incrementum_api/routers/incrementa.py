"""Controllers."""
__all__ = ["create_incrementa_router"]

from litestar import Router

from incrementum_api.controllers import IncrementaController


def create_incrementa_router() -> Router:
    """Create the router."""
    return Router(
        path="/v1",
        route_handlers=[IncrementaController],
    )
