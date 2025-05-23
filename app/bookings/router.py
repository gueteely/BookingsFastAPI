from fastapi import APIRouter, Depends
from app.bookings.service import BookingService
from app.users.models import Users
from app.users.dependecies import get_current_user
from datetime import date
from app.exceptions import RoomCannotBeBooked


router = APIRouter(
    prefix="/bookings",
    tags=["Bookings"]
)

@router.get("")
async def get_bookings(user: Users = Depends(get_current_user)):
    return await BookingService.find_all(user_id = user.id)

@router.post("")
async def add_booking(
    room_id: int, date_from: date, date_to: date,
    user: Users = Depends(get_current_user),
):
     booking = await BookingService.add(user.id, room_id, date_from, date_to)
     if not booking:
          raise RoomCannotBeBooked