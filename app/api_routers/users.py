from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
from starlette import status
from ..database import db, models
from ..utils import schema, hashing, oauth


router = APIRouter(
    prefix='/users',
    tags=['users']
)

@router.get('/', response_model=List[schema.User])
def get_users(db:Session=Depends(db.get_db), active_user=Depends(oauth.get_current_user)):
    return db.query(models.User).all()

@router.post('/', response_model=schema.User, status_code=status.HTTP_201_CREATED)
def create_user(payload:schema.UserCreate, db:Session=Depends(db.get_db)):
    payload.password= hashing.get_password_hash(payload.password)
    data = models.User(**payload.dict())
    db.add(data)
    db.commit()
    db.refresh(data)
    return data