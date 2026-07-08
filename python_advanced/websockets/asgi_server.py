#!/usr/bin/env python3

from starlette.responses import HTMLResponse
from starlette.routing import Route, WebSocketRoute
from starlette.applications import Starlette
from starlette.websockets import WebSocketDisconnect


async def homepage(request):
    return HTMLResponse("<h1>WebSocket App</h1>")


async def websocket_endpoint(websocket):
    await websocket.accept()
    try:
        while True:
            message = await websocket.receive_text()
            await websocket.send_text(message)
    except WebSocketDisconnect:
        print("Client disconnect")

app = Starlette(routes=[Route("/", homepage),
                        WebSocketRoute("/ws", websocket_endpoint)])
