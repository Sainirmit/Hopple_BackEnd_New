# Hopple Backend

## Overview

Hopple is an AI-driven project management system designed to dynamically create and manage sub-agents for various project tasks. The system ensures efficiency by putting sub-agents into a sleep mode after completing their tasks, reducing resource consumption while maintaining memory. The project manager (PM) has final approval over tasks before the sub-agents are terminated.

## Recent Updates

### 1. **Modularization of the PM Agent**

- Refactored `pm_agent.py` to separate core functionalities into dedicated modules:
  - **Task Creation** (`task_creator.py`)
  - **Priority Assignment** (`priority_assigner.py`)
  - **Worker Assignment** (`worker_assigner.py`)
  - **Meeting Summarization** (`meeting_summarizer.py`)
- This improves maintainability, readability, and testing.

### 2. **Sub-Agent Lifecycle Management**

- **Sleep Mode:** Sub-agents pause resource usage after completing their tasks but retain memory.
- **Final Approval Prompt:** The project manager is prompted before terminating sub-agents.

### 3. **Improved Logging**

- Added debug and info logs to track agent actions and ensure better debugging capabilities.

## Installation & Setup

### 1. **Clone the Repository**

```bash
git clone https://github.com/sainirmit/Hopple_BackEnd_New.git
cd Hopple_BackEnd_New
```

### 2. Set Up Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Tests

```bash
PYTHONPATH=. pytest
```

### 5. Run the Server

```bash
uvicorn server:app --reload
```

## The server will be available at http://127.0.0.1:8000.

# Directory Structure

```bash
Hopple_BackEnd_New/
├── agents/
│   ├── __init__.py
│   ├── pm_agent.py
│   └── pm/
│       ├── __init__.py
│       ├── task_creator.py
│       ├── priority_assigner.py
│       ├── worker_assigner.py
│       ├── meeting_summarizer.py
├── tests/
│   ├── test_pm_agent.py
│   ├── test_server.py
├── utils/
│   ├── __init__.py
│   ├── logger.py
│   ├── async_utils.py
├── requirements.txt
├── README.md
```

# Next Steps

- Implement more AI-driven prioritization logic.
- Enhance worker assignment using external HR database integration.
- Optimize sleep-mode efficiency for sub-agents.
- Expand the sub-agent ecosystem with additional agents (e.g., Risk Management, Budget Monitoring).

# Feel free to open an issue or submit a pull request if you have suggestions or improvements!

### Last updated: [23 February 2025]
