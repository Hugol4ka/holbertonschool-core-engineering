from starlette.applications import Starlette
from starlette.routing import Route, WebSocketRoute, Mount
from starlette.responses import HTMLResponse
from starlette.websockets import WebSocketDisconnect
from starlette.staticfiles import StaticFiles
import os

# 1. La page d'accueil qui lit index.html
async def homepage(request):
    path = os.path.join(os.path.dirname(__file__), "index.html")
    with open(path, "r", encoding="utf-8") as file:
        html_content = file.read()
    return HTMLResponse(html_content)

# 2. Le tunnel WebSocket
async def websocket_endpoint(websocket):
    await websocket.accept()
    try:
        while True:
            message = await websocket.receive_text()
            await websocket.send_text(message)
    except WebSocketDisconnect:
        print("Client disconnect")

# Le dossier courant où se trouvent index.html, chat.js et styles.css
current_dir = os.path.dirname(__file__)

# 3. L'application Starlette avec le support des fichiers statiques
app = Starlette(routes=[
    Route("/", homepage),
    WebSocketRoute("/ws", websocket_endpoint),
    # Cette ligne magique permet au navigateur de trouver chat.js et styles.css !
    Mount("/", app=StaticFiles(directory=current_dir), name="static")
])
