from fastapi import FastAPI

from app.routers import wrestlers, matches

# initialize instance of FastAPI class
app = FastAPI()


@app.get("/")
def wrestler():
    return { "status": "ok"}


app.include_router(wrestlers.router)
app.include_router(matches.router)
