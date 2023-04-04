from pydantic import BaseModel


class ConceptMapRequest(BaseModel):
    prompt: str
