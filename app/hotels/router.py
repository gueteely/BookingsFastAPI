from fastapi import APIRouter, Depends
from app.bookings.service import BookingService
from app.users.models import Users
from app.users.dependecies import get_current_user
from datetime import date
from app.exceptions import RoomCannotBeBooked


router = APIRouter(
    prefix="/hotels",
    tags=["Hotels!"]
)

@router.get("")
async def get_hotels():
    return await BookingService.find_all()
