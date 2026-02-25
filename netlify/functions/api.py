from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello from FastAPI on Netlify Functions!"}

# This is what Netlify calls
handler = Mangum(app)