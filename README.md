# Ollama Python API
A lightweight **FastAPI wrapper** for **Ollama**, providing a way to interact with local LLMs.

### Features
- **Health Checks:** Built-in monitoring for port `11434`.
- **Router:** Modular design using `APIRouter`.
- **Request Validation** using `pydantic`

## Installation
```bash
#clone repository
git clone https://github.com/oskiral/python-ollama-api.git
cd python-ollama-api

# install requirements
pip install -r requirements.txt
```

## How to run api?
```bash
uvicorn app.main:app --reload
```

## API Docs
| Method  | Endpoint |                   Description                    |
|:-------:|:--------:|:------------------------------------------------:|
|   GET   | /health  |           Checks if ollama is runing.            |
|  POST   |  /chat   | Sends message to ai model and returns resposne.  |