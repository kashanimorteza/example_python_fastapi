# webapi/api.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import route_a

#--------------------------------------------------------------------------------- [App]
api_key = "fd051ac1-e342-4631-968d-db3f19b575e7"
app = FastAPI(root_path=f"/{api_key}")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],       # Allow all origins
    allow_credentials=True,    # Allow credentials (if needed)
    allow_methods=["*"],       # Allow all HTTP methods
    allow_headers=["*"],       # Allow all headers
)

#--------------------------------------------------------------------------------- [Route]
app.include_router(route_a.api_router_a, prefix="/model_a", tags=["model_a"])

#--------------------------------------------------------------------------------- [Root]
@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}