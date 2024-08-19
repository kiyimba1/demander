from pydantic import BaseModel

class Question(BaseModel):
    content: str
    id: int
    author: str
    created_at: str
    updated_at: str
    vote_count: int
    topic: str