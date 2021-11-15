from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import db, models
from app.api_routers import (users, auth, tasks)

models.Base.metadata.create_all(bind=db.engine)

app= FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get('/')
def index():
    return {"message": "Hello World"}
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(tasks.router)


