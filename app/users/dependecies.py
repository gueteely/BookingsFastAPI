from fastapi import Request, HTTPException, Depends, status

from jose import jwt, JWTError
from app.config import setting
from datetime import datetime, timezone
from app.users.service import UsersService
from app.exceptions import TokenExpiredException, TokenAbsentException, IncorrectTokenFormatException, UserIsNotPresentException

def get_token(request: Request):
    token = request.cookies.get("booking_access_token")
    if not token:
        raise TokenAbsentException
    return token

async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(
            token, setting.SECRET_KEY, setting.HASH
        )
    except JWTError:
        raise IncorrectTokenFormatException
    expire: str = payload.get("exp")
    if (not expire) or (int(expire)) < datetime.now(timezone.utc).timestamp():
        raise TokenExpiredException
    user_id: str = payload.get("sub")
    if not user_id:
        raise UserIsNotPresentException
    user = await UsersService.find_by_id(int(user_id))
    if not user:
        raise UserIsNotPresentException

    return user