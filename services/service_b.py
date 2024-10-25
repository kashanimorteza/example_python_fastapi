# services/service_b.py

from typing import List
from models.model_b import model_b
from logics.logic_b import logic_b 
from fastapi import HTTPException

class service_b:
    def __init__(self, repository: logic_b):
        self.repository = repository

    async def create_item(self, item: model_b) -> model_b:
        created_item = await self.repository.create(item)
        if not created_item:
            raise HTTPException(status_code=400, detail="Item with this id already exists")
        return created_item

    async def get_items(self) -> List[model_b]:
        return await self.repository.get_all()

    async def get_item(self, item_id: int) -> model_b:
        item = await self.repository.get_by_id(item_id)
        if not item:
            raise HTTPException(status_code=404, detail="Item not found")
        return item

    async def update_item(self, item_id: int, item: model_b) -> model_b:
        updated_item = await self.repository.update(item_id, item)
        if not updated_item:
            raise HTTPException(status_code=404, detail="Item not found")
        return updated_item

    async def delete_item(self, item_id: int) -> dict:
        success = await self.repository.delete(item_id)
        if not success:
            raise HTTPException(status_code=404, detail="Item not found")
        return {"message": "Item deleted successfully"}