from enum import Enum
from typing import Union

import uvicorn as uvicorn
from fastapi import Depends, FastAPI
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.crud import crud
from app.database.config import SessionLocal

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root(db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email='sample')
    print(db_user)
    return {"message": "Hello FastAPI",
            "name": "Yusuke",
            "age": 26,
            "device": [
                "iPhone", "MacBook Air", "AppleWatch"
            ]}


@app.get("/items/{age}")
async def read_age(age: int):
    return {"message": "Hello FastAPI",
            "name": "Yusuke",
            "age": {age},
            }


class Fruits(str, Enum):
    apple = "Apple"
    banana = "Banana"
    peach = "Peach"


@app.get("/fruits/{fruits}")
async def get_fruits(fruits: Fruits):
    dic = {"message": "OK", "fruits": ""}

    if fruits is Fruits.apple:
        dic["fruits"] = Fruits.apple
    elif fruits is Fruits.banana:
        dic["fruits"] = Fruits.banana
    elif fruits is Fruits.peach:
        dic["fruits"] = Fruits.peach

    return dic


db_items = [
    {"item_name": "Foo"},
    {"item_name": "Bar"},
    {"item_name": "Buzz"},
]


@app.get("/search/{item_no}")
async def get_search(item_no: int, q: Union[str, None] = None):
    if q:
        return {"item": db_items[item_no], "q": q}
    return {"item": db_items[item_no]}


class Account(BaseModel):
    name: str
    description: Union[str, None] = None
    age: int


@app.post("/account/")
async def account(account: Account):
    return account


if __name__ == '__main__':
    uvicorn.run(app=app)
