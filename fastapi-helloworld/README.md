# FastAPI Hello World 

This is a basic FastAPI project to demonstrate a simple "Hello World" API.

##  Tech Stack

- **uv** - package manager
- **FastAPI** – Modern, fast web framework for building APIs with Python
- **Uvicorn** – ASGI server to run the FastAPI app
- **Python 3.10+**
- **PyTest** - Unit testing framework

##  Project Structure

fastapi-helloworld/
├── main.py
├── README.md
└── (venv or .env info)


## ▶️ How to Run

###  Install uv

Install uv on windows:
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

Install uv on mac and Linux
curl -LsSf https://astral.sh/uv/install.sh | less

#### Create a Project Directory and Switch to it
uv init folder_name
cd folder_name

pip install "fastapi[standard]" uvicorn

### Create and Activate the Virtual Environment

On macOS/Linux:

uv venv
source .venv/bin/activate
On Windows:

uv venv
.venv\Scripts\activate

### Install dependencies

uv add "fastapi[standard]"

uv add --dev pytest pytest-asyncio


### Run Server

fastapi dev main.py