from sqlalchemy import Column, Integer, String
from ..database import Base

class Driver(Base):
    __tablename__ = "drivers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    license_number = Column(String, nullable=False, unique=True)
    phone = Column(String, nullable=True)
    email = Column(String, nullable=True)
