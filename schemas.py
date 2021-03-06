from pydantic import BaseModel

class User(BaseModel):
    name: str
    phone: str

    class Config:
        orm_mode = True    
