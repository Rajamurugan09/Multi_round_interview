from pydantic import BaseModel


class RoundCreate(BaseModel):
    round_name: str
    score: int


class RoundResponse(BaseModel):
    id: int
    interview_id: int
    round_name: str
    score: int
    passed: bool

    class Config:
        from_attributes = True
