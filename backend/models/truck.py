from sqlalchemy import Column, Integer, String
from ..database import Base

class Truck(Base):
    __tablename__ = "trucks"

    id = Column(Integer, primary_key=True, index=True)
    unit_number = Column(String, unique=True, nullable=False)   # Truck number (e.g., T123)
    make = Column(String, nullable=True)                        # e.g., Volvo
    model = Column(String, nullable=True)                       # e.g., VNL760
    year = Column(Integer, nullable=True)                       # e.g., 2020
