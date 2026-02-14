from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.models.round import Round
from app.schemas.round import RoundCreate, RoundResponse

router = APIRouter(prefix="/rounds", tags=["Rounds"])


@router.post("/{interview_id}", response_model=RoundResponse)
def create_round(interview_id: int, data: RoundCreate, db: Session = Depends(get_db)):

    passed = data.score >= 60

    round_entry = Round(
        interview_id=interview_id,
        round_name=data.round_name,
        score=data.score,
        passed=passed
    )

    db.add(round_entry)
    db.commit()
    db.refresh(round_entry)

    return round_entry
