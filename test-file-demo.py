from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}
@app.get("/bye")
def read_root():
    return {"message": "bye, FastAPI!"}

@app.get("/greet/{name}")
def greet_name(name: str):
    return {"greeting": f"Hello, {name}!"}
