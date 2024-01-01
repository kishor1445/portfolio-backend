import os
import motor.motor_asyncio
from dotenv import load_dotenv

load_dotenv()

db_client = motor.motor_asyncio.AsyncIOMotorClient(os.getenv("MONGODB_URI"), ssl=True)
db = db_client.portfolio
