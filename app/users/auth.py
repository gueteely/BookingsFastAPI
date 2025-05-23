from passlib.context import CryptContext
from datetime import datetime, timezone, timedelta
from pydantic import EmailStr
from jose import jwt
from app.users.service import UsersService
from app.config import SECRET, HASH

pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password, hasherd_password):
    return pwd_context.verify(plain_password, hasherd_password)

def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, SECRET, HASH
    )
    return encoded_jwt


async def authenticate_user(email: EmailStr, password: str):
    user = await UsersService.find_one_or_none(emails = email)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user
    