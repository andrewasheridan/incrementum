__all__ = ["RedisSettings"]

from pydantic import RedisDsn

from incrementum_api.settings._base_env import BaseEnvSettings


class RedisSettings(BaseEnvSettings):
    """
    Cache settings for the application.

    Prefix all environment variables with `REDIS_`, e.g., `REDIS_URL`.

    Attributes:
    ----------
    URL : AnyUrl
        A redis connection URL.
    """

    class Config:
        env_prefix = "REDIS_"
        case_sensitive = True

    URL: RedisDsn = RedisDsn("redis://localhost:6379/0")
