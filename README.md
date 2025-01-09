# sustainable-manufacturing-tool

## Overview

This project provides an API that helps manufacturers identify sustainable materials, processes, and suppliers to create products in an environmentally friendly way. The tool analyzes the input product description and returns sustainable manufacturing alternatives, including raw material recommendations, sustainable processes, and eco-friendly shipping options.

## Features

- **Sustainable Manufacturing Process**: Identifies sustainable methods for producing the given product.
- **Alternative Raw Materials**: Suggests eco-friendly raw materials for product manufacturing.
- **Sustainable Process Development**: Outlines processes for manufacturing products sustainably.
- **Vendor Recommendations**: Provides a list of suppliers who offer sustainable materials and services.
- **Eco-friendly Shipping Options**: Suggests carbon-neutral or green shipping options.

## Technologies Used

- **Backend**: FastAPI (Python)
- **Environment**: Virtualenv, Python 3.x
- **Dependencies**: 
  - FastAPI
  - Uvicorn (ASGI server)
  - Pydantic (Data validation)
  
## Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Steps to Run the Application Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/sustainable-manufacturing-tool.git
   cd sustainable-manufacturing-tool

2. Set up a virtual environment:
   python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

3. Install dependencies:
   
   pip install -r requirements.txt

4. Run the FastAPI application locally:
   uvicorn app.main:app --reload

The application will now be running at http://127.0.0.1:8000. You can access the API documentation at http://127.0.0.1:8000/docs.

## API Endpoints

1. /sustainable-manufacturing (POST)
This endpoint accepts a product description and returns a response with sustainable manufacturing alternatives.

Request Body (JSON):

{
  "description": "Smartphone case made of plastic"
}

Response (JSON):

{
  "product": "Smartphone case made of plastic",
  "materials": [
    {
      "material": "Biodegradable Plastic",
      "description": "A plastic that decomposes naturally."
    },
    {
      "material": "Recycled Polyethylene",
      "description": "Made from recycled materials."
    }
  ],
  "process": "Use renewable energy for injection molding.",
  "vendors": [
    {
      "name": "EcoSupplier Inc.",
      "contact": "contact@ecosupplier.com"
    }
  ],
  "shipping": "Use carbon-neutral shipping methods."
}

2. / (GET)
The home endpoint that provides a simple message (optional):

Response (JSON):

{
  "message": "Welcome to the Sustainable Manufacturing Tool API!"
}


