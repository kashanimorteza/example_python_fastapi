#--------------------------------------------------------------------------------- Location
# webapi/services/service_log.py

#--------------------------------------------------------------------------------- Description
# This is Service for log

#--------------------------------------------------------------------------------- Import
from typing import List, Optional
from models.model_c import model_c as model
from logics.logic_c import logic_c as logic

#--------------------------------------------------------------------------------- Service
class service_c:
    #-------------------------- [Init]
    def __init__(self) : 
        self.logic = logic()

    #-------------------------- [Add]
    async def add(self, item:model) -> Optional[model] :
        return self.logic.add(item=item)

    #-------------------------- [Items]
    async def items(self) -> list[model] : 
        return self.logic.items()

    #-------------------------- [Item]
    async def item(self, id:int) -> Optional[model] :
        return self.logic.item(id=id)

    #-------------------------- [Update]
    async def update(self, id:int, item: model) -> Optional[model] :
        return self.logic.update(id=id, item=item)
    
    #-------------------------- [Delete]
    async def delete(self, id:int) -> bool :
        return self.logic.delete(id=id)