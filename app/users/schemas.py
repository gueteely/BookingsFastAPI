from pydantic import BaseModel, EmailStr

class SUserAuth(BaseModel):
    emails: EmailStr
    password: str 