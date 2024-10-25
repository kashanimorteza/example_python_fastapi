# webapi/api_b.py

#-------------------------- [Import]
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import route_b

#-------------------------- [Variable]
title = 'MKVPN'
key = "fd051ac1-e342-4631-968d-db3f19b575e7"
host  = '127.0.0.1'
port = 8000

#-------------------------- [App]
app = FastAPI(title=title, root_path=f"/{key}")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"], )

#-------------------------- [Route]
app.include_router(route_b.route, prefix="/model_b", tags=["model_b"])

#-------------------------- [Run]
if __name__ == "__main__":
    uvicorn.run(app, host=host, port=port)