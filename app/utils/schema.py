from datetime import datetime
from pydantic import BaseModel
from sqlalchemy import orm

class UserBase(BaseModel):
    email:str
    is_active:bool
class UserCreate(UserBase):
    password:str
class User(UserBase):
    id:int
    class Config:
        orm_mode=True
class UserOut(BaseModel):
    email:str
    class Config:
        orm_mode=True

class Login(BaseModel):
    email:str
    password:str
class Token(BaseModel):
    access_token:str
    token_type:str
class TokenData(BaseModel):
    id:int

class Task(BaseModel):
    id:str
    task:str
    completed:bool
    created_on:datetime
    owner:UserOut

    class Config:
        orm_mode=True
class TaskCreate(BaseModel):
    task:str