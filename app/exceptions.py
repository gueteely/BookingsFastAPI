from fastapi import HTTPException, status


class BookingException(HTTPException):
    def __init__(self, status_code=500, detail=None, headers=None):
        super().__init__(status_code=status_code, detail=detail, headers=headers)

class UserAlreadyExistsException(BookingException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail="User already exists"
        )

class IncorrectEmailOrPasswordException(BookingException):
       def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password"
        )

class TokenExpiredException(BookingException):
      def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token was expried"
        )

class TokenAbsentException(BookingException):
     def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Don't have a token"
        )

class IncorrectTokenFormatException(BookingException):
     def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect token format"
        )

class UserIsNotPresentException(HTTPException):
       def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
        )
class RoomCannotBeBooked(HTTPException):
       def __init__(self):
        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail="This room is busy!"
        )


