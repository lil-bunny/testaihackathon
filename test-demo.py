from fastapi import FastAPI
from tensorflow import keras

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/greet/{name}")
def greet_name(name: str):
    return {"greeting": f"Hello, {name}!"}