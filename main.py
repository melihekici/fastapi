import uvicorn
from fastapi import FastAPI
from schemas import User as SchemaUser
from fastapi_sqlalchemy import DBSessionMiddleware, db
import os
from dotenv import load_dotenv
from models import User as ModelUser

load_dotenv('.env')

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URL'])

@app.get('/')
async def root():
    return {"message": "Hello World"}

@app.post('/add-user/', response_model=SchemaUser)
def add_user(user: SchemaUser):
    db_user = ModelUser(name=user.name, phone=user.phone)
    db.session.add(db_user)
    db.session.commit()
    return db_user

@app.get('/users/')
def get_users():
    users = db.session.query(ModelUser).all()
    return users

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)