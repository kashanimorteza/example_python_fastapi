# services/service_a.py

from typing import List, Optional
from models.model_a import model_a 
from logics.logic_a import logic_a 

class service_a:

    #-------------------------- [Init]
    def __init__(self):
        self.logic = logic_a()

    #-------------------------- [List]
    def list(self) -> List[model_a]:
        return self.logic.list()
    
    #-------------------------- [Item]
    def item(self, id : int) -> Optional[model_a]:
        return self.logic.item(id = id)
    
    #-------------------------- [Add]
    def add(self, model : model_a) -> bool:
        return self.logic.add(model = model)
    
    #-------------------------- [Edit]
    def edit(self, model : model_a) -> bool:
        return self.logic.edit(model = model)
    
    #-------------------------- [Delete]
    def delete(self, id : int) -> bool:
        return self.logic.delete(id = id)