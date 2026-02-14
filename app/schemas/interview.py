from pydantic import BaseModel
from datetime import datetime


class InterviewCreate(BaseModel):
    candidate_name:str
    position:str

class InterviewResponse(BaseModel):
    id:int
    candidate_name:str
    position:str
    created_at:datetime

    class Config:
        from_attributes = True