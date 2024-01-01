from fastapi import FastAPI, status
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
from .routers import data

load_dotenv()

app = FastAPI()

for api in (data,):
    app.include_router(api.router)

@app.get("/ping", status_code=status.HTTP_200_OK)
def ping_test():
    return {"message": "pong!"}

app.mount(path="/static", app=StaticFiles(directory="static"), name="static")
