# webapi/routes/route_a.py

from fastapi import HTTPException, APIRouter
from models.model_a import model_a as model
from webapi.logic.logic_a import logic_a

#-------------------------- [Variable]
api_router_a = APIRouter()
logic = logic_a()

#-------------------------- [List]
@api_router_a.get("/list", description="Get list of  model_a")
def list():
    result = logic.list()
    if result["status"] :
        return result["data"]
    else:
        raise HTTPException(status_code=400, detail=result["data"])

#-------------------------- [Item]
@api_router_a.get("/item/{item}", description="get modele_a")
def item(item : str):
    result = logic.item(item=item)
    if result["status"] :
        return result["data"]
    else:
        raise HTTPException(status_code=400, detail=result["data"])

#-------------------------- [Add]
@api_router_a.post("/add", description="Add model_a")
def add(item : model):
    result = logic.add(item=item)
    if result["status"] :
        return result["data"]
    else:
        raise HTTPException(status_code=400, detail=result["data"])

#-------------------------- [Edit]
@api_router_a.post("/edit", description="Edit config of xray")
def edit(item : model):
    result = logic.edit(item=item)
    if result["status"] :
        return result["data"]
    else:
        raise HTTPException(status_code=400, detail=result["data"])

#-------------------------- [Delete]
@api_router_a.post("/delete", description="Delete model_a")
def delete(item : model):
    result = logic.delete(item=item)
    if result["status"] :
        return result["data"]
    else:
        raise HTTPException(status_code=400, detail=result["data"])
    
#-------------------------- [Test]
def test():

    #---List
    params = logic.list()
    print(params)

    #---Item
    params = logic.item('A')
    print(params)

    #---Model
    o = model
    o.id = 1
    o.name = "morteza"
    
    #---Add
    params = logic.add(o)
    print(params)

    #---Edit
    params = logic.edit(o)
    print(params)

    #---Delete
    params = logic.delete(o)
    print(params)