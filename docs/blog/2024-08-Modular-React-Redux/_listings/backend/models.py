from pydantic import BaseModel

class ValueResponse(BaseModel):
    value: int
