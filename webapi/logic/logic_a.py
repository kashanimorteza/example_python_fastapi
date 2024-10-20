# webapi/logic/model_a.py

from models.model_a import model_a as model
from libs.lib_a import lib_a

class logic_a:

    #-------------------------- [Init]
    def __init__(self):
        self.lib = lib_a()

    #-------------------------- [List]
    def list(self) -> dict:
        params={}
        return self.lib.list(params)
    
    #-------------------------- [Item]
    def item(self, item : str) -> str:
        params = {"item" : item}
        return self.lib.item(params)
    
    #-------------------------- [Add]
    def add(self, item : model) -> dict:
        params = {"item" : item}
        return self.lib.add(params)
    
    #-------------------------- [Edit]
    def edit(self, item : model) -> dict:
        params = {"item" : item}
        return self.lib.edit(params)
    
    #-------------------------- [Delete]
    def delete(self, item : model) -> dict:
        params = {"item" : item}
        return self.lib.delete(params)