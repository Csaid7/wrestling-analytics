from fastapi import FastAPI
# initialize instance of FastAPI class
app = FastAPI()
@app.get("/")
def wrestler():
    return { "status": "ok"}
    