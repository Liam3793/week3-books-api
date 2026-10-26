from pydantic import BaseModel, ConfigDict, Field


class BookCreate(BaseModel):

    title: str= Field(min_length=2, max_length=100)
    author: str = Field(min_length = 2, max_length=100)
    year: int = Field(ge =  1900)

class BookResponse(BaseModel):
    id: int
    title: str
    author:str
    year: int

    model_config = ConfigDict(from_attributes=True)
    
 
