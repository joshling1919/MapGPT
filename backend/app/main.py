from fastapi import FastAPI, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
import openai

from .config import MONGODB_URL, DATABASE_NAME, OPENAI_API_KEY
from .models.concept_map import ConceptMapRequest
from .templates.prompts import concept_map_template

openai.api_key = OPENAI_API_KEY
app = FastAPI()


@app.on_event("startup")
async def startup_event():
    mongodb_url = MONGODB_URL
    database_name = DATABASE_NAME

    app.mongodb_client = AsyncIOMotorClient(mongodb_url)
    app.mongodb = app.mongodb_client[database_name]


@app.get("/")
async def root():
    return {"message": "Hello, FastAPI!"}


@app.post("/generate_concept_map")
async def generate_concept_map(request: ConceptMapRequest):
    topic = request.prompt
    try:
        formatted_prompt = concept_map_template.format(topic=topic)
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=formatted_prompt,
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.5,
        )

        concept_map = response.choices[0].text.strip()

        # Convert the generated concept map text to JSON format
        # You can modify this part according to the expected format of the concept map
        concept_map_json = {"concept_map": concept_map}

        return concept_map_json
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
