import uvicorn
from litestar import Litestar

from emirecorder.config.models import Config


class Server:
    """Server for the application.

    Args:
        app: The application.
        config: The configuration for the application.
    """

    def __init__(self, app: Litestar, config: Config) -> None:
        self._app = app
        self._config = config

    def run(self) -> None:
        """Run the server."""

        config = self._config.server

        uvicorn.run(
            self._app,
            host=config.host,
            port=config.ports.http,
        )
