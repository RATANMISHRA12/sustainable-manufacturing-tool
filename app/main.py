from fastapi import FastAPI
from pydantic import BaseModel
import json
from app.utils import get_sustainable_materials, get_sustainable_process, format_output

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the Sustainable Manufacturing Tool API!"}

class ProductRequest(BaseModel):
    description: str
    budget: str = None
    material_restrictions: str = None

@app.post("/sustainable-manufacturing")
async def get_sustainable_alternatives(request: ProductRequest):
    materials = get_sustainable_materials(request.description)
    process = get_sustainable_process(request.description)
    
    output = format_output(request.description, materials, process)
    return output
