from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from models import Note,User
from schemas import NoteCreate,NoteResponse,NoteUpdate
from auth.deps import get_current_user



router=APIRouter(prefix="/notes",tags=["notes"])


@router.post("/",response_model=NoteResponse)
def create_note(
    note:NoteCreate,
    db: Session=Depends(get_db),
    current_user:User=Depends(get_current_user)
):
    new_note=Note(title=note.title,content=note.content,user_id=current_user.id)
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    
    return new_note

@router.get("/",response_model=List[NoteResponse])
def get_note(
    db:Session=Depends(get_db),
    current_user: User=Depends(get_current_user)
):
    notes=db.query(Note).filter(Note.user_id==current_user.id).all()
    return notes

@router.get("/{note_id}",response_model=NoteResponse)
def getbyid(
    note_id:int,
    db:Session=Depends(get_db),
    current_user:User=Depends(get_current_user)
):
    note=(db.query(Note).filter(Note.id==note_id,Note.user_id==current_user.id).first()) #two conditions to check id match and user_id match so that other people cant access.
    
    if not note:
        raise HTTPException(status_code=404,detail="Note not found")
    
    return note
    
@router.put("/",response_model=NoteResponse)
def update(
    id:int,
    noteupdate:NoteUpdate,
    db:Session=Depends(get_db),
    current_user:User=Depends(get_current_user)
):
    note=(db.query(Note).filter(Note.id==id,Note.user_id==current_user.id).first())

    if not note:
        raise HTTPException(status_code=404,detail="not found")
    
    update_data=noteupdate.model_dump(exclude_unset=True)

    for key,value in update_data.items():
        setattr(note,key,value)

        db.commit()
        db.refresh(note)
        return note

@router.delete("/")
def delete(
    id:int,
    db:Session=Depends(get_db),
    current_user:User=Depends(get_current_user)
):
    note=(db.query(Note).filter(Note.id==id,Note.user_id==current_user.id).first())
    if not Note:
        raise HTTPException(status_code=404,detail="Not found")
    db.delete(note)
    db.commit()
    return {"message":"Note Deleted "}