import json
from app.models import Material, Vendor, Output

def load_data(file_name: str):
    with open(f"app/{file_name}") as f:
        return json.load(f)

materials_data = load_data("materials.json")
processes_data = load_data("processes.json")
vendors_data = load_data("vendors.json")

def get_sustainable_materials(description: str):
    return materials_data[:2]

def get_sustainable_process(description: str):
    return processes_data[0]["process"]

def format_output(product_description: str, materials, process):
    vendors = [Vendor(name=vendor["name"], contact=vendor["contact"]) for vendor in vendors_data]
    
    return Output(
        product=product_description,
        materials=materials,
        process=process,
        vendors=vendors,
        shipping="Use carbon-neutral shipping methods."
    )
