import asyncio
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from pydantic import BaseModel  # note: BaseModel is capitalized (uppercase B and M)
from datetime import datetime

app = FastAPI()

class Command(BaseModel):
    id: int
    action: str
    timestamp: datetime

commands: list[Command] = []

@app.get("/commands")
def read_commands():
    return commands

@app.post("/commands")
def create_command(cmd: Command):
    commands.append(cmd)
    return {"status": "ok", "id": cmd.id}

class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, ws: WebSocket):
        await ws.accept()
        self.active_connections.append(ws)
    
    def disconnect(self, ws: WebSocket):
        self.active_connections.remove(ws)
    
    async def broadcast(self, message: dict):
        for connection in list(self.active_connections):
            try:
                await connection.send_json(message)
            except WebSocketDisconnect:
                self.disconnect(connection)

manager = ConnectionManager()

@app.websocket("/ws/telemetry")
async def telemetry_endpoint(ws: WebSocket):
    """
    WebSocket route at /ws/telemetry:
    - accepts new connections
    - continuously sends dummy or real telemetry updates every second.
    """
    await manager.connection(ws)
    try:
        while True:
            #replace this dict with real data from your drone/pymavlink
            data = {
                "altitude": 120.5,
                "speed": 5.2,
                "battery": 87,
                "timestamp": asyncio.get_event_loop().time()
            }
            await manager.broadcast(data)
            await asyncio.sleep(1)
    except WebSocketDisconnect:
        manager.disconnect(ws)
