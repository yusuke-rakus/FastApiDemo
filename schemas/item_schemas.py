from pydantic import BaseModel


class Item(BaseModel):
    item_id: str
    user_id: str
    title: str
    description: str
