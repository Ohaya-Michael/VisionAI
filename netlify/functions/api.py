from fastapi import FastAPI
from mangum import Mangum
from pydantic import BaseModel

app = FastAPI()

@app.get("/api/hello")
def hello():
    return {"message": "Hello from FastAPI on Netlify Functions!"}

# This is what Netlify calls
handler = Mangum(app)