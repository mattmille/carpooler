from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from datetime import datetime
from enum import Enum

app = FastAPI()

class Travel_Time(Enum):
    Morning = 1
    Afternoon = 2
    Night = 3

# Simple in-memory storage for this example
trips = []

class Trip(BaseModel):
    user_name: str
    departure_date: datetime
    departure_time: str
    return_date: datetime
    return_time: str

@app.post("/trips/")
async def create_trip(trip: Trip):
    trips.append(trip)
    return {"message": "Trip created successfully"}

@app.get("/trips/")
async def get_trips():
    return trips
