from sqlalchemy.orm import Session

from forms.user_forms import LoginForm, CreateUserForm, DeleteUserForm
from models import models


def get_user(db: Session, user_id: int, email: str):
    return db.query(models.User).filter(models.User.user_id == user_id).filter(models.User.email == email).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def login(db: Session, user: LoginForm):
    return db.query(models.User).filter(models.User.email == user.email).first()


def create_user(db: Session, user: CreateUserForm):
    user_model = models.User(email=user.email)
    db.add(user_model)
    db.commit()
    db.refresh(user_model)
    return user_model


def delete_user(db: Session, user: DeleteUserForm):
    db_user = get_user(db=db, user_id=user.user_id, email=user.email)
    if db_user is not None:
        try:
            db.delete(db_user)
            db.commit()
            return 'delete successful'
        except Exception:
            return 'delete failed'
    return db_user


def select_all_user_with_item(db: Session):
    user = models.User
    item = models.Item
    return db.query(user, item).outerjoin(item, item.user_id == user.user_id).all()
