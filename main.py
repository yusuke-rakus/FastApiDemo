import uvicorn as uvicorn
from fastapi import FastAPI

from endpoints.item import router as item_router
from endpoints.user import router as user_router

app = FastAPI()

app.include_router(user_router, tags=['user'])
app.include_router(item_router, tags=['item'])

if __name__ == '__main__':
    uvicorn.run(app=app)
