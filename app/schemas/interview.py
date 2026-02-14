from pydantic import BaseModel
from datetime import datetime
from app.models.interview import InterviewStatus

class InterviewCreate(BaseModel):
    candidate_name:str
    position:str

class InterviewResponse(BaseModel):
    id:int
    candidate_name:str
    position:str
    created_at:datetime
    status: InterviewStatus

    class Config:
        from_attributes = True
        use_enum_values = True