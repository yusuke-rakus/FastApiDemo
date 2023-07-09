from fastapi import APIRouter

from database.config import SessionLocal

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/item")
async def router_sample():
    return {
        "sample": "item"
    }
