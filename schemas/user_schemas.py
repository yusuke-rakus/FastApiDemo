from typing import List

from pydantic import BaseModel

from schemas.item_schemas import Item


class UserBase(BaseModel):
    email: str
    user_id: int

    class Config:
        orm_mode = True


class User(UserBase):
    items: List[Item]
