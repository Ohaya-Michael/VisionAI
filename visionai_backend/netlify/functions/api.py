from fastapi import FastAPI
from mangum import Mangum
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello from FastAPI on Netlify!"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "status": "success"}

# This is the entry point for Netlify Functions
handler = Mangum(app)