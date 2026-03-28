# Assisted by ChatGPT
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello World"}

@app.get("/data")
def get_data():
    return {
        "name": "Rahail",
        "course": "AI-ML",
        "status": "learning Docker"
    }