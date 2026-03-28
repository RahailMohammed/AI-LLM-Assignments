# Assignment 2 - Basic Backend API & Docker Deployment

## Objective
This project demonstrates:
- Creating a simple backend API using FastAPI
- Dockerizing the application
- Running the application inside a container

## Endpoints
- / → Returns Hello World
- /data → Returns sample JSON


## Run locally

```bash
pip install -r requirements.txt
uvicorn app:app --reload