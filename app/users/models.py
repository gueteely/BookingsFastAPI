from app.database import Base
from sqlalchemy import Column, Integer, String, JSON, ForeignKey, Date, Computed

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key =True, nullable=False)
    emails = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)