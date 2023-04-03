import os
from dotenv import load_dotenv
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv()

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    mongodb_url = os.environ["MONGODB_URL"]
    database_name = os.environ["DATABASE_NAME"]

    app.mongodb_client = AsyncIOMotorClient(mongodb_url)
    app.mongodb = app.mongodb_client[database_name]


@app.on_event("shutdown")
async def shutdown_event():
    app.mongodb_client.close()


@app.get("/")
async def root():
    return {"message": "Hello, FastAPI!"}
