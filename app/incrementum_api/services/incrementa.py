"""IncrementaService."""

__all__ = ["IncrementaService"]

from redis.asyncio import Redis

from incrementum_api import settings


class IncrementaService:
    """IncrementaService."""

    def __init__(self) -> None:
        """Create the IncrementaService."""
        self._redis = Redis.from_url(settings.redis.URL.unicode_string())

    async def create_new_counter(self, name: str, /, *, amount: int = 1) -> int:
        """Create a new counter."""
        return await self.reset_counter(name, amount=amount)

    async def get_next_value(self, name: str, /) -> int:
        """Get the next counter value."""
        return await self._redis.incr(name=name)

    async def get_current_value(self, name: str, /) -> int | None:
        """Get the current value without incrementing it."""
        result: bytes | None = await self._redis.get(name=name)

        if result is not None:
            return int(result.decode())

        return result

    async def reset_counter(self, name: str, /, *, amount: int = 1) -> int:
        """Reset counter."""
        await self._redis.delete(name)
        return await self._redis.incr(name=name, amount=amount)
