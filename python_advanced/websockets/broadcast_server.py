#!/usr/bin/env python3

import asyncio
import websockets
from websockets.exceptions import ConnectionClosed

connected_clients = set()

async def connection_handler(websocket):
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            for client in connected_clients:
                    await client.send(f"B:{message}")
    except ConnectionClosed:
        print("Client disconnected")
    finally:
        connected_clients.remove(websocket)


async def main():
    async with websockets.serve(connection_handler, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
