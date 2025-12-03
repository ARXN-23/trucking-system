from pydantic import BaseModel

class TruckBase(BaseModel):
    unit_number: str
    make: str | None = None
    model: str | None = None
    year: int | None = None

class TruckCreate(TruckBase):
    pass

class TruckResponse(TruckBase):
    id: int

    class Config:
        orm_mode = True
