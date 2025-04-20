```python
from fastapi import FastAPI
# from pandas import keras # pandas doesn't have keras. If you intend to use keras, install tensorflow and import keras from tensorflow
# from tensorflow import keras # uncomment this line if you intend to use keras

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}


@app.get("/greet/{name}")
def greet_name(name: str):
    return {"greeting": f"Hello, {name}!"}
```