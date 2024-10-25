# routes/route_b.py

#-------------------------- [Import]
from fastapi import APIRouter
from models.model_b import model_b
from logics.logic_b import logic_b 
from services.service_b import service_b
from typing import List

#-------------------------- [Variable]
route = APIRouter()
logic = logic_b()
service = service_b(logic)

#-------------------------- [Create]
@route.post("/items/", response_model=model_b)
async def create_item(item: model_b):
    """Create a new item"""
    return await service.create_item(item)

#-------------------------- [Items]
@route.get("/items/", response_model=List[model_b])
async def read_items():
    """Get all items"""
    return await service.get_items()

#-------------------------- [Item]
@route.get("/items/{item_id}", response_model=model_b)
async def read_item(item_id: int):
    """Get a specific item by ID"""
    return await service.get_item(item_id)

#-------------------------- [Update]
@route.put("/items/{item_id}", response_model=model_b)
async def update_item(item_id: int, item: model_b):
    """Update an item"""
    return await service.update_item(item_id, item)

#-------------------------- [Delete]
@route.delete("/items/{item_id}")
async def delete_item(item_id: int):
    """Delete an item"""
    return await service.delete_item(item_id)