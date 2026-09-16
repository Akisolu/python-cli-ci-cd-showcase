from pydantic import BaseModel, Field

class OpcionInput(BaseModel):
    # Validate an integer strictly within the 1 to 4 range.
    opcion: int = Field(..., ge=1, le=4)