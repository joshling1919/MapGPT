from fastapi import FastAPI, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
import openai

from config import OPENAI_API_KEY
from models.concept_map import ConceptMapRequest
from templates.prompts import concept_map_template, system_prompt_template
from fastapi.middleware.cors import CORSMiddleware

openai.api_key = OPENAI_API_KEY
app = FastAPI()

origins = [
    "http://localhost:5173",  # Replace this with the origin of your frontend app
    # Add any other origins you need
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello, FastAPI!"}


@app.post("/generate_concept_map")
async def generate_concept_map(request: ConceptMapRequest):
    topic = request.prompt
    try:
        # Construct the chat prompt as a list of messages
        messages = [
            {
                "role": "system",
                "content": system_prompt_template
            },
            {
                "role": "user",
                "content": concept_map_template.format(topic=topic)
            }
        ]

        # Call openai.createChatCompletion to generate the concept map
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
        )

        concept_map = response.choices[0].message.content.strip()

        # Convert the generated concept map text to JSON format
        # You can modify this part according to the expected format of the concept map
        concept_map_json = {"concept_map": concept_map}

        return concept_map_json
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
