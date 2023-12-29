"""Settings."""
__all__ = ["app", "redis", "server"]
from incrementum_api.settings._app import AppSettings
from incrementum_api.settings._redis import RedisSettings
from incrementum_api.settings._server import ServerSettings

app = AppSettings()
redis = RedisSettings()
server = ServerSettings()
