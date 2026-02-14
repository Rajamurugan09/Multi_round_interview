from sqlalchemy import Column,Integer ,String,DateTime
from sqlalchemy.sql import func
from app.database.base import Base
from sqlalchemy import Enum
import enum


class InterviewStatus(enum.Enum):
    APPLIED = "APPLIED"
    ROUND1 = "ROUND1"
    ROUND2 = "ROUND2"
    ROUND3 = "ROUND3"
    REJECTED = "REJECTED"
    SELECTED = "SELECTED"

class Interview(Base):
    __tablename__ = "interviews"

    id=Column(Integer, primary_key=True, index=True)
    candidate_name=Column(String)
    position=Column(String)
    created_at=Column(DateTime(timezone=True), server_default=func.now())
    status = Column(Enum(InterviewStatus), default=InterviewStatus.APPLIED)