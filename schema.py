from pydantic import BaseModel
from typing import Optional

class PersonResponse(BaseModel):
    name:str
    id:int

class PersonQuery(BaseModel):
    name:Optional[str]
    id:Optional[str]

class PersonCreate(BaseModel):
    name:str
