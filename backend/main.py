from fastapi import FastAPI
from .database import engine, Base
from .routers import driver_router, truck_router

app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(driver_router.router)
app.include_router(truck_router.router)

@app.get("/")
def root():
    return {"message": "Trucking system API running"}
