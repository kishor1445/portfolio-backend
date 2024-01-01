import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import motor.motor_asyncio
from dotenv import load_dotenv
from .routers import data

load_dotenv()

app = FastAPI()

for api in (data,):
    app.include_router(api.router)

app.mount(path="/static", app=StaticFiles(directory="static"), name="static")
