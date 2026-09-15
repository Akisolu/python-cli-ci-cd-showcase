from pydantic import BaseModel, Field

class IdInput(BaseModel):
    # Validate an integer strictly greater than or equal to 1.
    id_comida: int = Field(..., gt=0)