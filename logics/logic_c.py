#--------------------------------------------------------------------------------- location
# logics/logic_c.py

#--------------------------------------------------------------------------------- Description
# This is logic of logic_c

#--------------------------------------------------------------------------------- Import
import asyncio
from typing import List, Optional
from models.model_c import model_c as model

#--------------------------------------------------------------------------------- Logic
class logic_c:
    #-------------------------- [Init]
    def __init__(self):
        self.db: List[model] = [] 

    #-------------------------- [Add]
    async def add(self, item:model) -> Optional[model]:
        if any(x.id == item.id for x in self.db): return None
        self.db.append(item)
        await asyncio.sleep(2)
        return item

    #-------------------------- [Items]
    async def items(self) -> Optional[List[model]] :
        await asyncio.sleep(2)
        return self.db

    #-------------------------- [Item]
    async def item(self, id:int) -> Optional[model]:
        await asyncio.sleep(2)
        return next((x for x in self.db if x.id == id), None)

    #-------------------------- [Update]
    async def update(self, id:int, item:model) -> Optional[model]:
        index = next((i for i, x in enumerate(self.db) if x.id == id), None)
        if index is None:
            return None
        item.id = id
        self.db[index] = item
        await asyncio.sleep(2)
        return item

    #-------------------------- [Delete]
    async def delete(self, id:int) -> bool:
        index = next((i for i, x in enumerate(self.db) if x.id == id), None)
        if index is None:
            return False
        self.db.pop(index)
        await asyncio.sleep(2)
        return True
