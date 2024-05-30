from pydantic import BaseModel

class Msg(BaseModel):
    id: int
    content: str
    datetime: str