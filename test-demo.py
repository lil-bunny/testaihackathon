```python
from fastapi import FastAPI
# from pandas import keras # pandas doesn't have keras

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}


@app.get("/greet/{name}")
def greet_name(name: str):
    return {"greeting": f"Hello, {name}!"}
```