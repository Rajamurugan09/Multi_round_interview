from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session


from app.database.session import get_db
from app.models.interview import Interview
from app.schemas.interview import InterviewCreate, InterviewResponse

router = APIRouter(
    prefix="/interviews",
    tags=["Interviews"]
)

@router.post("/", response_model=InterviewResponse)
def create_interview(
    data: InterviewCreate,
    db: Session = Depends(get_db)
):
    interview = Interview(
        candidate_name=data.candidate_name,
        position=data.position
    )
    db.add(interview)
    db.commit()
    db.refresh(interview)
    return interview


@router.get("/",response_model=list[InterviewResponse])
def list_interview(db:Session = Depends(get_db)):
    return db.query(Interview).all()