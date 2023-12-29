"""IncrementaService."""

__all__ = ["IncrementaService"]


from redis.asyncio import Redis

from incrementum_api import settings

_redis = Redis.from_url(settings.redis.URL.unicode_string(), health_check_interval=30)


class IncrementaService:
    """IncrementaService."""

    async def create_new_counter(self, name: str, /, *, amount: int = 1) -> int:
        """Create a new counter."""
        return await self.reset_counter(name, amount=amount)

    @staticmethod
    async def get_next_value(name: str, /) -> int:
        """Get the next counter value."""
        return await _redis.incr(name=name)

    @staticmethod
    async def get_current_value(name: str, /) -> int | None:
        """Get the current value without incrementing it."""
        result: bytes | None = await _redis.get(name=name)

        if result is not None:
            return int(result.decode())

        return result

    @staticmethod
    async def reset_counter(name: str, /, *, amount: int = 1) -> int:
        """Reset counter."""
        await _redis.delete(name)
        return await _redis.incr(name=name, amount=amount)
