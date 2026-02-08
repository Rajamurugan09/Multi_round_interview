from sqlalchemy import Column,Integer ,String,DateTime
from sqlalchemy.sql import func
from app.database.base import Base

class Interview(Base):
    __tablename__ = "interview"

    id=Column(Integer, primary_key=True, index=True)
    candidate_name=Column(String)
    position=Column(String)
    created_at=Column(DateTime(timezone=True), server_default=func.now())