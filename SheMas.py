from typing import Optional
from pydantic import BaseModel


class STaskadd(BaseModel):
    name: str
    description: Optional[str] = None

class STask(BaseModel):
    id: int

    class Config:
        from_attributes = True