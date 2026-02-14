from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.models.interview import Interview
from app.schemas.interview import InterviewCreate, InterviewResponse

router = APIRouter(prefix="/interviews", tags=["Interviews"])


@router.post("/", response_model=InterviewResponse)
def create_interview(data: InterviewCreate, db: Session = Depends(get_db)):
    interview = Interview(
        candidate_name=data.candidate_name,
        position=data.position
    )
    db.add(interview)
    db.commit()
    db.refresh(interview)
    return interview


@router.get("/", response_model=list[InterviewResponse])
def list_interviews(db: Session = Depends(get_db)):
    return db.query(Interview).all()


@router.delete("/{interview_id}")
def delete_interview(interview_id: int, db: Session = Depends(get_db)):
    interview = db.query(Interview).filter(Interview.id == interview_id).first()
    if not interview:
        raise HTTPException(status_code=404, detail="Interview not found")
    db.delete(interview)
    db.commit()
    return {"message": "Interview deleted"}
