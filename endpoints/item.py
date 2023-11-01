from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud import item_crud
from database.config import SessionLocal
from forms.itme_form import InsertItemForm, DeleteItemForm, UpdateItemForm

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get('/item/{item_id}')
async def get_item_by_id(item_id: int, db: Session = Depends(get_db)):
    db_item = item_crud.get_item_by_id(db=db, item_id=item_id)
    return db_item


@router.get('/item/userId/{user_id}')
async def get_item_by_user_id(user_id: int, db: Session = Depends(get_db)):
    db_item = item_crud.get_item_by_user_id(db=db, user_id=user_id)
    return db_item


@router.post('/item/create')
async def create_item(item: InsertItemForm, db: Session = Depends(get_db)):
    db_item = item_crud.insert_item(db=db, form=item)
    return db_item


@router.post('/item/delete')
async def delete_item(item: DeleteItemForm, db: Session = Depends(get_db)):
    db_item = item_crud.delete_item(db=db, form=item)
    return db_item


@router.post('/item/update')
async def update_item(item: UpdateItemForm, db: Session = Depends(get_db)):
    db_item = item_crud.update_item(db=db, form=item)
    return db_item
