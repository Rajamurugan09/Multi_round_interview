from sqlalchemy.orm import declarative_base

Base = declarative_base()


from app.models.interview import Interview
from app.models.round import Round