from __future__ import annotations

import logging
from abc import ABC
from typing import Any

from websockets.client import WebSocketClientProtocol

logger = logging.getLogger('async_websocket_client')


class BaseDispatcher(ABC):
    """Базовый класс диспетчера"""

    app: Any
    ws: WebSocketClientProtocol

    is_running: bool

    def __init__(self) -> None:
        self.is_running = False

    def set_app(self, app: Any):
        self.app = app

    async def set_websocket(self, ws: WebSocketClientProtocol):
        self.ws = ws

    async def before_connect(self):
        logger.info('before_connect')

    async def on_connect(self):
        logger.info('on_connect')
        self.is_running = True

    async def before_disconnect(self):
        logger.info('before_disconnect')
        self.is_running = False

    async def on_disconnect(self):
        logger.info('on_disconnect')

    async def on_message(self, message: str):
        logger.info(f'client | on_message: {message}')
