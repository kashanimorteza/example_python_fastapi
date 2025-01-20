#--------------------------------------------------------------------------------- Location
# models/model_c.py

#--------------------------------------------------------------------------------- Description
# This is model_c

#--------------------------------------------------------------------------------- Import
from pydantic import BaseModel, Field

#--------------------------------------------------------------------------------- Model
class model_c(BaseModel):
    id: int = Field(default=1, description="The unique identifier for model_c")
    name: str = Field(default="model_c", description="The name of model_c")