from typing import List, Optional
from pydantic import BaseModel


class Foo(BaseModel):
    count: int
    size: Optional[float]

