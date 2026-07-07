#!/usr/bin/env python3

import websockets
import asyncio
import os


async def connect_and_send(uri, message):
    if "WS_URI" in os.environ:
        uri = os.environ["WS_URI"]

    async with websockets.connect(uri) as websocket:
        await websocket.send(message)
        response = await websocket.recv()
        print(response, end="")
        return response

if __name__ == "__main__":
    asyncio.run(connect_and_send("ws://localhost:8765", "demo"))
