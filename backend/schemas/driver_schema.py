from pydantic import BaseModel

class DriverBase(BaseModel):
    name: str
    license_number: str
    phone: str | None = None
    email: str | None = None

class DriverCreate(DriverBase):
    pass

class DriverResponse(DriverBase):
    id: int

    class Config:
        orm_mode = True
