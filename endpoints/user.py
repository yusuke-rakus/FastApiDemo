from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud import crud
from database.config import SessionLocal
from forms.user_forms import UserForm

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/user")
async def router_sample():
    return {
        "sample": "user"
    }


@router.post("/user/getUser")
async def root(user: UserForm, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    return db_user
