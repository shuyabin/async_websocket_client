# Async WebSocket client

A module that implements an asynchronous interface based on [websockets](https://github.com/python-websockets/websockets) for working with websockets

[![PyPI](https://img.shields.io/pypi/v/async-websocket-client)](https://pypi.org/project/async-websocket-client/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/async-websocket-client)](https://pypi.org/project/async-websocket-client/)
[![GitLab last commit](https://img.shields.io/gitlab/last-commit/rocshers/python/async-websocket-client)](https://gitlab.com/rocshers/python/async-websocket-client)

[![Test coverage](https://codecov.io/gitlab/rocshers:python/async-websocket-client/branch/release/graph/badge.svg?token=RPFNZ8SBQ6)](https://codecov.io/gitlab/rocshers:python/async-websocket-client)
[![Downloads](https://static.pepy.tech/badge/async-websocket-client)](https://pepy.tech/project/async-websocket-client)
[![GitLab stars](https://img.shields.io/gitlab/stars/rocshers/python/async-websocket-client)](https://gitlab.com/rocshers/python/async-websocket-client)

## Functionality

- Регистрация / Удаление WS
- Создание / Удаление групп WS
- Подключение WS в группу
- Поддержка реестров: memory, redis

## Quick start

Установка:

```sh
pip install async-websocket-client
```

Подключение:

```python
import asyncio
from async_websocket_client.apps import AsyncWebSocketApp
from async_websocket_client.dispatchers import BaseDispatcher

class SomeDispatcher(BaseDispatcher):
    async def on_connect(self):
        return await self.ws.send('hello, server')

    async def on_message(self, message: str):
        return await self.ws.send(f'server, I received your message. len(message)=={len(message)}')

client = AsyncWebSocketApp('ws://localhost:8001/ws', SomeDispatcher())
client.asyncio_run() # quick run
# or
asyncio.run(client.run()) # Run with asyncio
```
