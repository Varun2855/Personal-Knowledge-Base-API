from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from database import get_db
from auth.deps import get_current_user
from models import User

from ai.schemas import AskRequest,AskResponse
from ai.service import build_context,askllm

router=APIRouter(prefix="/ai",tags=["AI"])

@router.post("/ask",response_model=AskRequest)
def ask_ai(data:AskRequest,db:Session=Depends(get_db),current_user: User=Depends(get_current_user)):
    context=build_context(db,current_user.id)
    answer=askllm(data.question,context)

    return{"answer":answer}