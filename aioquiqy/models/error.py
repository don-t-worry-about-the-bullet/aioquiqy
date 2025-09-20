from pydantic import BaseModel, Field
from typing import Optional


class HTTPError(BaseModel):
    """HTTP error response model"""
    
    hint: Optional[str] = Field(None, description="Optional hint for error handling")
    msg: str = Field(..., description="Error message")
