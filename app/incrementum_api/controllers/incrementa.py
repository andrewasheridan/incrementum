"""IncrementaController."""
__all__ = ["IncrementaController"]

from typing import final

from litestar import Controller, get, post
from litestar.di import Provide
from litestar.dto import DTOData
from litestar.exceptions import NotFoundException

from exemplars.incrementum import (
    Incrementum,
    IncrementumReadDTO,
    IncrementumWriteDTO,
)
from incrementum_api.services import IncrementaService


@final
class IncrementaController(Controller):
    """IncrementaController."""

    path = "/incrementa"
    """The path fragment for the controller."""

    dto = IncrementumReadDTO
    """Serializing and validation of request data."""

    return_dto = IncrementumWriteDTO
    """Serializing outbound response data."""

    dependencies = {"incrementa_service": Provide(dependency=IncrementaService, sync_to_thread=False)}
    """A string keyed dictionary of dependency :class:`Provider <.di.Provide>` instances."""

    @get("/{nomen:str}/deinde")
    async def get_next_value(self, nomen: str, incrementa_service: IncrementaService) -> Incrementum:
        """Get the next counter value."""
        result = await incrementa_service.get_next_value(nomen)
        return Incrementum(nomen=nomen, valorem=result)

    @get("/{nomen:str}/nunc")
    async def get_current_value(self, nomen: str, incrementa_service: IncrementaService) -> Incrementum:
        """Get the current value without incrementing it."""
        result = await incrementa_service.get_current_value(nomen)
        # or await incrementa_service.create_new#_counter(nomen)
        if result is None:
            raise NotFoundException(f"Incrementum named {nomen} not found.")

        return Incrementum(nomen=nomen, valorem=result)

    @post("/{nomen:str}/reset")
    async def reset(self, data: DTOData[Incrementum], incrementa_service: IncrementaService) -> Incrementum:
        """Reset the counter."""
        incrementum = data.create_instance()
        result = await incrementa_service.reset_counter(incrementum.nomen, amount=incrementum.valorem)
        incrementum.valorem = result
        return incrementum
