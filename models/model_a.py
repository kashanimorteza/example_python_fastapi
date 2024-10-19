# models/model_a.py

from pydantic import BaseModel

class model_a(BaseModel):
    id : int = 1
    name : str = "model-a"