from fastapi import FastAPI, Query, Depends
from typing import Optional
from datetime import date
from pydantic import BaseModel
from app.bookings.router import router as router_bookings
from app.users.router import router as router_users
from app.pages.router import router as router_pages

app = FastAPI()

app.include_router(router_users)
app.include_router(router_bookings)
app.include_router(router_pages)

class HotelsSearchArgs:
    def __init__(
            self, 
            location: str,
            date_from: date, 
            date_to: date,
            has_spa: Optional[bool] = None,
            starts: Optional[int] = Query(None, ge=1, le=5)
    ):
        self.location = location
        self.date_from =  date_from
        self.date_to = date_to
        self.has_spa = has_spa
        self.starts = starts

class SHotel(BaseModel):
    address: str
    name: str
    stars: int


@app.get("/hotels")
def get_hotels(
    search_args: HotelsSearchArgs = Depends()
) -> list[SHotel]:
    hotels = [
        {"address": "Street 13, Altay",
         "name": "Super Hotel",
         "stars": 5}
    ]
    return hotels
