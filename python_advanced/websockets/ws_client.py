#!/usr/bin/env python3

import websockets
import asyncio
import os


async def connect_and_send(uri, message):
    async with websockets.connect(uri) as websocket:
        await websocket.send(message)
        response = await websocket.recv()
        print(response, end="")
        return response

async def main():
    uri = os.environ.get("WS_URI", "ws://127.0.0.1:8765")
    await connect_and_send(uri, "Hello WebSocket")

if __name__ == "__main__":
    asyncio.run(connect_and_send("ws://localhost:8765", "Hello WebSocket"))
