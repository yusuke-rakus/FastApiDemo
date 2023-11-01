from sqlalchemy.orm import Session

from forms.itme_form import InsertItemForm, DeleteItemForm, UpdateItemForm
from models import models


def get_item(db: Session, item_id: int, user_id: int):
    return db.query(models.Item).filter(models.Item.item_id == item_id).filter(models.Item.user_id == user_id).first()


def get_item_by_id(db: Session, item_id: int):
    return db.query(models.Item).filter(models.Item.item_id == item_id).first()


def get_item_by_user_id(db: Session, user_id: int):
    return db.query(models.Item).filter(models.Item.user_id == user_id).all()


def insert_item(db: Session, form: InsertItemForm):
    item_model = models.Item(title=form.title, description=form.description, user_id=form.user_id)
    db.add(item_model)
    db.commit()
    db.refresh(item_model)
    return item_model


def update_item(db: Session, form: UpdateItemForm):
    db_item = get_item(db=db, item_id=form.item_id, user_id=form.user_id)
    if db_item is not None:
        db_item.title = form.title
        db_item.description = form.description
        db.commit()
        db.refresh(db_item)
    return db_item


def delete_item(db: Session, form: DeleteItemForm):
    db_item = get_item(db=db, item_id=form.item_id, user_id=form.user_id)
    if db_item is not None:
        try:
            db.delete(db_item)
            db.commit()
            return 'delete successful'
        except Exception:
            return 'delete failed'
    return db_item
