from fastapi import FastAPI
from core.models import model

app = FastAPI()

@app.get("/")
def hello_world():
    return {"message": "Hello, World!"}


@app.post("/chat")
def chat(message: str):
    return {"message": model.invoke(message)}


