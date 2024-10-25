# logics/logic_b.py

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
