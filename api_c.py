#--------------------------------------------------------------------------------- Location
# api_c.py

#--------------------------------------------------------------------------------- Description
# This is api_c.py

#--------------------------------------------------------------------------------- Import
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import route_c

#-------------------------- [Variable]
title = 'api_c'
key = "aaaa"
description="This is api_c"
version="1.0.0"
openapi_url=f"/schema"
docs_url=f"/doc1"
redoc_url=f"/doc2"
# docs_url=None
# redoc_url=None
host = '0.0.0.0'
port = 8000

#-------------------------- [App]
app = FastAPI(
    title=title,
    description=description,
    version=version,
    openapi_url=openapi_url,
    docs_url=docs_url,
    redoc_url=redoc_url,
    root_path=f"/{key}"
)
app.add_middleware(
    CORSMiddleware, 
    allow_origins=["*"], 
    allow_credentials=True, 
    allow_methods=["*"], 
    allow_headers=["*"]
) 

#-------------------------- [Route]
app.include_router(route_c.route_c_api, prefix="/model_c", tags=["model_c"])


#-------------------------- [Run]
if __name__ == "__main__":
    uvicorn.run(app, host=host, port=port)