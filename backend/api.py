from fastapi import FastAPI
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