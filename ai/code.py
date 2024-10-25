# Content of file api_b.py

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import route_b

#-------------------------- [Variable]
title = 'MKVPN'
key = "fd051ac1-e342-4631-968d-db3f19b575e7"
host  = '127.0.0.1'
port = 8000

#-------------------------- [App]
app = FastAPI(title=title, root_path=f"/{key}")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"], )

#-------------------------- [Route]
app.include_router(route_b.route, prefix="/model_b", tags=["model_b"])

#-------------------------- [Run]
if __name__ == "__main__":
    uvicorn.run(app, host=host, port=port)



# Content of file routes/route_b.py

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
@route.post("/items/", description="Create", response_model=model_b)
async def create_item(item: model_b):
    """Create a new item"""
    return await service.create_item(item)

#-------------------------- [Items]
@route.get("/items/", description="Items", response_model=List[model_b])
async def read_items():
    """Get all items"""
    return await service.get_items()

#-------------------------- [Item]
@route.get("/items/{item_id}", description="Item", response_model=model_b)
async def read_item(item_id: int):
    """Get a specific item by ID"""
    return await service.get_item(item_id)

#-------------------------- [Update]
@route.put("/items/{item_id}", description="Update", response_model=model_b)
async def update_item(item_id: int, item: model_b):
    """Update an item"""
    return await service.update_item(item_id, item)

#-------------------------- [Delete]
@route.delete("/items/{item_id}", description="Delete", )
async def delete_item(item_id: int):
    """Delete an item"""
    return await service.delete_item(item_id)


# content of file services/service_b.py

from typing import List
from models.model_b import model_b
from logics.logic_b import logic_b 
from fastapi import HTTPException


class service_b:
    #-------------------------- [Init]
    def __init__(self, logic: logic_b):
        self.logic = logic

    #-------------------------- [Create]
    async def create_item(self, item: model_b) -> model_b:
        created_item = await self.logic.create(item)
        if not created_item:
            raise HTTPException(status_code=400, detail="Item with this id already exists")
        return created_item

    #-------------------------- [Items]
    async def get_items(self) -> List[model_b]:
        return await self.logic.get_all()

    #-------------------------- [Item]
    async def get_item(self, item_id: int) -> model_b:
        item = await self.logic.get_by_id(item_id)
        if not item:
            raise HTTPException(status_code=404, detail="Item not found")
        return item
    
    #-------------------------- [Update]
    async def update_item(self, item_id: int, item: model_b) -> model_b:
        updated_item = await self.logic.update(item_id, item)
        if not updated_item:
            raise HTTPException(status_code=404, detail="Item not found")
        return updated_item

    #-------------------------- [Delete]
    async def delete_item(self, item_id: int) -> dict:
        success = await self.logic.delete(item_id)
        if not success:
            raise HTTPException(status_code=404, detail="Item not found")
        return {"message": "Item deleted successfully"}
    

# content of file logics/logic_b.py

from typing import List, Optional
from models.model_b import model_b

class logic_b:
    #-------------------------- [Init]
    def __init__(self):
        self.db: List[model_b] = []  # In-memory storage for demonstration

    #-------------------------- [Create]
    async def create(self, item: model_b) -> model_b:
        if any(x.id == item.id for x in self.db):
            return None
        self.db.append(item)
        return item

    #-------------------------- [Items]
    async def get_all(self) -> List[model_b]:
        return self.db

    #-------------------------- [Item]
    async def get_by_id(self, item_id: int) -> Optional[model_b]:
        return next((x for x in self.db if x.id == item_id), None)

    #-------------------------- [Update]
    async def update(self, item_id: int, item: model_b) -> Optional[model_b]:
        index = next((i for i, x in enumerate(self.db) if x.id == item_id), None)
        if index is None:
            return None
        item.id = item_id
        self.db[index] = item
        return item

    #-------------------------- [Delete]
    async def delete(self, item_id: int) -> bool:
        index = next((i for i, x in enumerate(self.db) if x.id == item_id), None)
        if index is None:
            return False
        self.db.pop(index)
        return True
    
# content of file models/model_b.py

from pydantic import BaseModel, Field

class model_b(BaseModel):
    id: int = Field(default=1, description="The unique identifier for model_b")
    name: str = Field(default="model-b", description="The name of model_b")
