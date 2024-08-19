from pydantic import BaseModel

class Answer(BaseModel):
    answer: str
    id: int
    author: str
    created_at: str
    updated_at: str
    upvote_count: int
    downvote_count: int