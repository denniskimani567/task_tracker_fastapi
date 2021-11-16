# FastAPI Task Tracker, using OAuth2 with Password, Password Hashing and JWT Token 
Link to project (https://morning-gorge-07253.herokuapp.com/docs)

Minimalistic Task Tracker Web API built with FastAPI. 

# Getting started:
To clone the project, run:
```
git clone https://github.com/denniskimani567/task_tracker_fastapi.git
cd task_tracker_fastapi
```
create .env file 
```
DATABASE_URL={database_url}
SECRET_KEY = {secret_key}
ALGORITHM = HS256
ACCESS_TOKEN_EXPIRE_MINUTES = {desire minutes}`
```
To generate a secret_key that will be used to sign JWT tokens run:
```
openssl rand -hex 32
```
