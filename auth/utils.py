from passlib.context import CryptContext

pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")

def hashpassword(password:str)->str:
    return pwd_context.hash(password)

def verifypassword(password:str,hashed_password:str)->bool:
    return pwd_context.verify(password,hashed_password)