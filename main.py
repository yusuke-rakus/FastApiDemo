from enum import Enum
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def root():
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
