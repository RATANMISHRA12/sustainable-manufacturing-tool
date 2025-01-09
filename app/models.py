from pydantic import BaseModel
from typing import List

class Material(BaseModel):
    material: str
    description: str

class Vendor(BaseModel):
    name: str
    contact: str

class Output(BaseModel):
    product: str
    materials: List[Material]
    process: str
    vendors: List[Vendor]
    shipping: str
