from typing import Optional
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"hello": "world"}

@app.get("/stuff/{thing_id}")
def read_thing(thing_id: int, name: Optional[str] = None):
    return {"id": thing_id, "info": name}