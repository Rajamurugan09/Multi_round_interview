from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from app.database.base import Base


class Round(Base):
    __tablename__ = "rounds"

    id = Column(Integer, primary_key=True, index=True)
    interview_id = Column(Integer, ForeignKey("interviews.id"))
    round_name = Column(String, nullable=False)
    score = Column(Integer)
    passed = Column(Boolean, default=False)
