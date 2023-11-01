from pydantic import BaseModel


class InsertItemForm(BaseModel):
    title: str
    description: str
    user_id: int


class UpdateItemForm(BaseModel):
    item_id: int
    title: str
    description: str
    user_id: int


class DeleteItemForm(BaseModel):
    item_id: int
    user_id: int
