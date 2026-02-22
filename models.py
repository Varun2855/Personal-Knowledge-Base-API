from sqlalchemy import Integer,String,Column,ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    
    __tablename__= "users2"

    id=Column(Integer,primary_key=True, unique=True, index=True)
    email=Column(String,unique=True,index=True,nullable=False)    
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    notes=relationship("Note",back_populates="owner")

class Note(Base):
    __tablename__="notes2"

    id=Column(Integer,primary_key=True,unique=True,index=True)
    title=Column(String,nullable=False)
    content=Column(String,nullable=False)

    user_id=Column(Integer,ForeignKey("users2.id"),nullable=False)

    owner=relationship("User",back_populates="notes") #User.notes  <------>  Note.owner


