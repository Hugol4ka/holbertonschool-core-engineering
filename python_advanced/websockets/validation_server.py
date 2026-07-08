#!/usr/bin/env python3

import asyncio
import websockets


async def connection_handler(websocket):
    async for message in websocket:
        message_clean = message.strip()

        if not message_clean:
            await websocket.send("ERR:EMPTY")
        else:
            await websocket.send(f"OK:{message_clean}")


async def main():
    async with websockets.serve(connection_handler, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
