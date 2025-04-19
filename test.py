from fastapi import FastAPI

app = FastAPI()



@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}


@app.get("/say_bye")
def read_root():
    return {"message": "bye bye"}

@app.get("/say_bye2")
def read_root():
    return {"message": "bye bye"}


@app.get("/greet/{name}")
def greet_name(name: str):
    return {"greeting": f"Hello, {name}!"}
