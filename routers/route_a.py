# routes/route_a.py

from turtle import mode
from fastapi import HTTPException, APIRouter
from models.model_a import model_a
from services.service_a import service_a

#-------------------------- [Variable]
api_router_a = APIRouter()
service = service_a()

#-------------------------- [List]
@api_router_a.get("/list", description="Get list of items")
def list():
    result = service.list()
    return result

#-------------------------- [Item]
@api_router_a.get("/item/{id}", description="Get item based on id")
def item(id : int):
    result = service.item(id)
    return result

#-------------------------- [Add]
@api_router_a.post("/add", description="Add item")
def add(model : model_a):
    result = service.add(model = model)
    return result

#-------------------------- [Edit]
@api_router_a.post("/edit", description="Edit item")
def edit(model : model_a):
    result = service.edit(model = model)
    return result

#-------------------------- [Delete]
@api_router_a.get("/delete/{id}", description="Delete item based on id")
def delete(id : int):
    result = service.delete(id = id)
    return result

#-------------------------- [Test]
def test():

    #---List
    params = service.list()
    print(params)

    #---Item
    params = service.item('A')
    print(params)

    #---Model
    o = model_a()
    o.id = 1
    o.name = "morteza"
    
    #---Add
    params = service.add(o)
    print(params)

    #---Edit
    params = service.edit(o)
    print(params)

    #---Delete
    params = service.delete(o)
    print(params)