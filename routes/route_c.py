#--------------------------------------------------------------------------------- Location
# routes/route_c.py

#--------------------------------------------------------------------------------- Description
# This is Route for route_c

#--------------------------------------------------------------------------------- Import
from typing import List, Optional
from fastapi import APIRouter
from models.model_c import model_c as model
from services.service_c import service_c as service

#--------------------------------------------------------------------------------- Route
#-------------------------- [Variable]
route_c_api = APIRouter()
service = service()

#-------------------------- [Add]
@route_c_api.get("/", description="default", response_model=Optional[model])
async def default() : 
    return model()

#-------------------------- [Add]
@route_c_api.post("/add", description="Add item", response_model=Optional[model])
async def add(item:model) : 
    return service.add(item=item)

#-------------------------- [Items]
@route_c_api.get("/items", description="Retrun list of items", response_model=List[model])
async def items() : 
    return service.items()

#-------------------------- [Item]
@route_c_api.get("/item/{id}", description="Return item", response_model=Optional[model])
async def item(id:int) : 
    return service.item(id=id)

#-------------------------- [Update]
@route_c_api.put("/update/{id}", description="Update item", response_model=Optional[model])
async def update(id:int, item: model) : 
    return service.update(id=id, item=item)

#-------------------------- [Delete]
@route_c_api.get("/delete/{id}", description="Delete item", response_model=bool)
async def item(id:int) : 
    return service.delete(id=id)