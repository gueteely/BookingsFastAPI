from app.database import Base
from sqlalchemy import Column, Integer, String, JSON, ForeignKey, Date, Computed

class Rooms(Base):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key =True, nullable=False)
    hotel_id = Column(Integer, ForeignKey("hotels.id"), nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Integer, nullable=False)
    services = Column(JSON, nullable=True)
    quantity = Column(Integer, nullable=False)
    image_id = Column(Integer)