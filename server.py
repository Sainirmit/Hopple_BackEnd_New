from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import subprocess

app = FastAPI()

# Enable CORS for development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Hopple AI Agent API is running!"}

@app.get("/generate/")
def generate_text(prompt: str):
    try:
        # Run the Ollama command with the prompt to generate a response
        result = subprocess.run(
            ["ollama", "run", "mistral", prompt],
            capture_output=True, text=True
        )
        return {"response": result.stdout.strip()}
    except Exception as e:
        return {"error": str(e)}
