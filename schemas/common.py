from typing import Optional

from pydantic import BaseModel


class CommonParams(BaseModel):
    q: Optional[str] = None
    limit: int = 100
    skip: int = 0
