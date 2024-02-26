from fastapi import FastAPI 
from datetime import datetime
from typing import Annotated, List, Optional
import uuid
from fastapi import FastAPI, HTTPException, Response
import motor.motor_asyncio
from dotenv import dotenv_values
from pydantic import BaseModel, BeforeValidator, Field, TypeAdapter 
from bson import ObjectId
from pymongo import ReturnDocument

config = dotenv_values(".env")

config["MONGO_URL"] 

client = motor.motor_asyncio.AsyncIOMotorClient(config["MONGO_URL"])

db = client.tank_man

app = FastAPI() 

PyObjectId = Annotated[str, BeforeValidator(str)]

class Tank(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    location: Optional[str] = None
    lat: Optional[float] = None
    long: Optional[float] = None 

class Profile(BaseModel): 
    id: Optional[PyObjectId] = Field(alias = "_id", default = None)
    last_updated: Optional[str] = None
    username: Optional[str] = None
    role: Optional[str] = None
    color: Optional[str] = None


@app.get("/tank")
async def get_tanks():
    tanks = await db["tanks"].find().to_list(999)
    return TypeAdapter(List[Tank]).validate_python(tanks)

@app.get("/tank/{id}")
async def get_tank(id: str):
    tank = await db["tanks"].find_one({"_id": ObjectId(id)})
    if tank is None:
        raise HTTPException(status_code = 404, detail = "Tank of id: " + id + " not found.")
    return Tank(**tank)

@app.post("/tank", status_code=201)
async def create_tank(tank: Tank):
    new_tank = await db["tanks"].insert_one(tank.model_dump())
    created_tank = await db["tanks"].find_one({"_id": new_tank.inserted_id})

    await update_profile()

    return Tank(**created_tank)

@app.patch("/tank/{id}")
async def update_tank(id: str, tank_update: Tank):
    updated_tank = await db["tanks"].update_one(
        {"_id": ObjectId(id)},
        {"$set": tank_update.model_dump(exclude_unset=True)},
    )
    await update_profile()

    if updated_tank.modified_count > 0:
        patched_tank = await db["tanks"].find_one(
            {"_id": ObjectId(id)}
        )
        
        return Tank(**patched_tank)
    
    raise HTTPException(status_code = 404, detail = "Tank of id: " + id + " not found.")

@app.delete("/tank/{id}")
async def delete_tank(id: str):
    deleted_tank = await db["tanks"].delete_one({"_id": ObjectId(id)})
    await update_profile()

    if deleted_tank.deleted_count < 1:
        raise HTTPException(status_code = 404, detail = "Tank of id: " + id + " not found.")
    
    return Response(status_code = 204)