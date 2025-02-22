# server.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from hopple_core import HoppleCore
import asyncio

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Hopple AI Agent API is running!"}

@app.get("/generate/")
async def generate_text(prompt: str):
    try:
        # Asynchronously run the Ollama command using asyncio.create_subprocess_exec
        proc = await asyncio.create_subprocess_exec(
            "ollama", "run", "mistral", prompt,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await proc.communicate()
        if proc.returncode != 0:
            return {"error": stderr.decode().strip()}
        return {"response": stdout.decode().strip()}
    except Exception as e:
        return {"error": str(e)}

@app.get("/process/")
async def process_task(task: str):
    """
    Asynchronously process a high-level task.
    """
    hopple = HoppleCore()
    plan = await hopple.process_task(task)
    return {"plan": plan}
