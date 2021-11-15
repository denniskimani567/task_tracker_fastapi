from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security.oauth2 import  OAuth2PasswordRequestForm
from typing import List
from sqlalchemy.orm import Session
from app.utils import hashing
from ..database import db, models
from ..utils import schema, oauth


router = APIRouter()

@router.post('/login', response_model=schema.Token)
def login(payload:OAuth2PasswordRequestForm = Depends(), db:Session=Depends(db.get_db)):
    user= db.query(models.User).filter(models.User.email == payload.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid Credentials')
    if not hashing.verify_hash(payload.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid Credentials')
    access_token= oauth.create_access_token(data={"user_id":user.id})
    return {"access_token": access_token, "token_type":"Bearer"}

