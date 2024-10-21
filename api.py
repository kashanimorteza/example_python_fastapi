# webapi/api.py

from fastapi import FastAPI
from routers import route_a

#-------------------------- [app]
api_key = "fd051ac1-e342-4631-968d-db3f19b575e7"
app = FastAPI(root_path=f"/{api_key}")

#-------------------------- [Route]
app.include_router(route_a.api_router_a, prefix="/model_a", tags=["model_a"])

#-------------------------- [Root]
@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}

#-------------------------- [Test]
#route_a.test()