from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud import user_crud
from database.config import SessionLocal
from forms.user_forms import LoginForm, CreateUserForm, DeleteUserForm

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post('/user/login')
async def login(user: LoginForm, db: Session = Depends(get_db)):
    db_user = user_crud.login(db, user=user)
    return db_user


@router.post('/user/create')
async def create_user(user: CreateUserForm, db: Session = Depends(get_db)):
    db_user = user_crud.create_user(db=db, user=user)
    return db_user


@router.post('/user/delete')
async def create_user(user: DeleteUserForm, db: Session = Depends(get_db)):
    db_user = user_crud.delete_user(db=db, user=user)
    return db_user


@router.get('/user/showAll')
async def sample(db: Session = Depends(get_db)):
    return user_crud.select_all_user_with_item(db=db)
