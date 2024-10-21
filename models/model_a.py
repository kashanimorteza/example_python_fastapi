# models/model_a.py

from pydantic import BaseModel, Field

class model_a(BaseModel):
    id: int = Field(default=1, description="The unique identifier for model_a")
    name: str = Field(default="model-a", description="The name of model_a")
