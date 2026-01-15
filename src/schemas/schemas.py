from pydantic import BaseModel
from typing import List


class Material(BaseModel):
    name: str
    qty: int | float
    price_rub: float


class MaterialsData(BaseModel):
    materials: List[Material]
