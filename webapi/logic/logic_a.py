# webapi/logic/model_a.py

from httpx import delete
from models.model_a import model_a as model
from libs.lib_a import lib_a as lib

class logic_a:

    #-------------------------- [Init]
    def __init__(self):
        self.logic = lib()

    #-------------------------- [List]
    def list(self) -> dict:
        params={}
        return self.logic.list(params)
    
    #-------------------------- [Item]
    def item(self, item : str) -> str:
        params = {"item" : item}
        return self.logic.item(params)
    
    #-------------------------- [Add]
    def add(self, item : model) -> dict:
        params = {"item" : item}
        return self.logic.add(params)
    
    #-------------------------- [Edit]
    def edit(self, item : model) -> dict:
        params = {"item" : item}
        return self.logic.edit(params)
    
    #-------------------------- [Delete]
    def delete(self, item : model) -> dict:
        params = {"item" : item}
        return self.logic.delete(params)
    

