from fastapi import FastAPI
from database import engine
import models
from auth.router import router as auth_router
from notes.router import router as notes_router
from ai.router import router as ai_router


app=FastAPI()
models.Base.metadata.create_all(bind=engine)
app.include_router(auth_router)
app.include_router(notes_router)
app.include_router(ai_router)