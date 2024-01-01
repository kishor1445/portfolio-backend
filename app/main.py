from fastapi import FastAPI, status
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from .routers import data

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

for api in (data,):
    app.include_router(api.router)

@app.get("/ping", status_code=status.HTTP_200_OK)
def ping_test():
    return {"message": "pong!"}

app.mount(path="/static", app=StaticFiles(directory="static"), name="static")
