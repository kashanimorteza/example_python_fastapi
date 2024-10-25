# models/model_a.py

from pydantic import BaseModel, Field

class model_b(BaseModel):
    id: int = Field(default=1, description="The unique identifier for model_b")
    name: str = Field(default="model-b", description="The name of model_b")