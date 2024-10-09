from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from parcel_handler import ParcelHandler, DepartmentFactory

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Parcel(BaseModel):
    name: str
    weight: float
    value: float
    department: str

class Parcels(BaseModel):
    parcels: List[Parcel]

@app.get("/parcels", response_model=Parcels)
async def get_parcels():
    handler = ParcelHandler("Container_68465468.xml")
    parcels = handler.parse_parcels()

    factory = DepartmentFactory()
    processed_parcels = []

    for parcel in parcels:
        department = factory.get_department(parcel['weight'], parcel['value'])
        department.process(parcel)
        processed_parcels.append(
            Parcel(
                name=parcel['name'],
                weight=parcel['weight'],
                value=parcel['value'],
                department=department.__class__.__name__
            )
        )
    
    return Parcels(parcels=processed_parcels)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
