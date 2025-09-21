from pydantic import BaseModel, Field
from typing import Optional

class HTTPError(BaseModel):
    hint: Optional[str]
    msg: str
