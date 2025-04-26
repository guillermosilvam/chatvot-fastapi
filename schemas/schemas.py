from pydantic import BaseModel

class Bot(BaseModel):
    id: int
    prompt: str
