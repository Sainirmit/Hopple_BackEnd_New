# Hopple_BackEnd_New

This repository contains the backend for **Hopple**, an AI Agent marketplace product. It is built using FastAPI and integrates with local AI models (via Ollama and Mistral).

## Features

- FastAPI server with CORS enabled
- Root endpoint `/` to verify the server is running
- Endpoint `/generate/` to generate AI responses based on a prompt
- Endpoint `/process/` to process high-level tasks by delegating to sub-agents (e.g., a Project Management sub-agent)
- Robust logging using a custom logger (located in `utils/logger.py`)
- Modular architecture with a meta-agent (`HoppleCore`) that can dynamically spawn sub-agents

## Getting Started

### Prerequisites

- Python 3.9+
- FastAPI and Uvicorn
- Ollama installed (for running the AI models locally)
- Git for version control

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sainirmit/Hopple_BackEnd_New.git
   ```
   **Navigate to the project directory:**
   ```bash
   cd Hopple_BackEnd_New
   ```
   **Create a virtual environment and activate it:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
   **Install dependencies:**
   ```bash
   pip install fastapi uvicorn pytest
   ```
   **Run the FastAPI server:**
   ```bash
   uvicorn server:app --reload
   ```

## The server will be available at http://127.0.0.1:8000.

###Testing

##Local Testing:

- Integration tests are located in the tests/ folder. To run tests, execute:
  PYTHONPATH=. pytest

-Continuous Integration:
-A GitHub Actions workflow is set up in .github/workflows/ci.yml to automatically run tests on every push or pull request.
