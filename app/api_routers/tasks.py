from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session
from ..database import db, models
from ..utils import schema,oauth

router = APIRouter(
    prefix='/tasks',
    tags=['tasks']
)

@router.get('/', response_model=List[schema.Task])
def get_tasks(db:Session = Depends(db.get_db), active_user:int=Depends(oauth.get_current_user)):
    return  db.query(models.Task).all()

@router.post('/', response_model=schema.Task, status_code=status.HTTP_201_CREATED)
def create_tasks(payload: schema.TaskCreate, db: Session= Depends(db.get_db), active_user:int=Depends(oauth.get_current_user)):
    data= models.Task(owner_id= active_user.id, **payload.dict())
    db.add(data)
    db.commit()
    db.refresh(data)
    return data