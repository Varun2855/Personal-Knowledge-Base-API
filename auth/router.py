from fastapi import APIRouter,Depends,HTTPException,status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import get_db
from models import User
from schemas import UserCreate
from auth.utils import hashpassword,verifypassword
from auth.jwt import create_access_token


router=APIRouter(prefix="/auth",tags=["auth"])

@router.post("/register",status_code=201)
def register(user:UserCreate,db:Session=Depends(get_db)):
    if db.query(User).filter(User.email==user.email).first():
        raise HTTPException(status_code=400,detail="User exists already")
    
    new_user=User(email=user.email,username=user.username,hashed_password=hashpassword(user.password))

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return{"message":"Created sucessfully"}

@router.post("/login")
def login(form_data:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    identifier=form_data.username

    user=(db.query(User).filter((User.email==identifier)|(User.username==identifier)).first())

    if not user or not verifypassword(form_data.password,user.hashed_password):
        raise HTTPException(status_code=401,detail="Invalid Credentials")
    
    token=create_access_token({"sub":str(user.id)})
    return {"access_token":token, "token_type":"bearer"}


    