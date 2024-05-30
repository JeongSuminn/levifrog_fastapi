from pydantic import BaseModel

class Todo(BaseModel):
    id: int
    content: str
    datetime: str