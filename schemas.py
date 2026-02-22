from pydantic import BaseModel,EmailStr

class UserCreate(BaseModel):
    email:EmailStr
    username:str
    password:str

class UserResponse(BaseModel):
    id:int
    email:EmailStr

    class Config:
        form_attributes:True

class NoteCreate(BaseModel):
    title:str
    content:str

class NoteUpdate(BaseModel):
    title:str|None=None
    content:str|None=None


class NoteResponse(BaseModel):
    id:int
    title:str
    content:str
    user_id:int


class config:
    orm_mode:True
    

