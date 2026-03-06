from models import Note
from sqlalchemy.orm import Session
import requests
from dotenv import load_dotenv
import os

load_dotenv()

OPENROUTER_API_KEY=os.getenv("OPENROUTER_API_KEY")
OPENROUTER_MODEL=os.getenv("OPENROUTER_MODEL")

def build_context(db:Session,user_id:int)->str:
    notes=db.query(Note).filter(Note.user_id==user_id).all()
    context="\n\n".join(f"Title:{n.title}\n Content:{n.content}"
                        for n in notes)
    return context

def askllm(question:str,context:str)->str:

    prompt=f"""
You are a personal knowledge assistant

You are to answer ONLY using the notes below.

NOTES:
{context}

QUESTION:
{question}
"""
    response=requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization":f"Bearer {OPENROUTER_API_KEY}",
            "HTTP-Referer": "http://localhost:8000",
            "X-Title": "Personal Knowledge Base",
            "Content-Type":"application/json",
        },
        json={
            "model":OPENROUTER_MODEL,
            "messages":[
                {"role":"user","content":prompt}
            ],
        },
    )

    data=response.json()

    if "choices" not in data:
        raise Exception(f"OpenRouter error: {data}")
    
    return data["choices"][0]["message"]["content"]




