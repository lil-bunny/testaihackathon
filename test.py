dfrom fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/greet/{name}")sdfdsf
def greet_name(name: str):
    return {"greeting": f"Hello, {name}!"}

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}
