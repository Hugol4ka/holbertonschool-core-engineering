#!/usr/bin/env python3

import websockets
import asyncio


async def connect_and_send(url, message):
    async with websockets.connect(url) as websocket:
        await websocket.send(message)
        response = await websocket.recv()
        print(f"{response}")


if __name__ == "__main__":
    asyncio.run(connect_and_send("ws://localhost:8765", "Hello WebSocket"))
