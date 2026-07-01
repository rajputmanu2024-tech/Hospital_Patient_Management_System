from fastapi import FastAPI, Path , HTTPException,Query
from fastapi.responses import JSONResponse
import json
from pydantic import BaseModel,Field,computed_field,EmailStr
from typing import Annotated,Literal

class Address(BaseModel):
    city: Annotated[str, Field(...,description="city where the patient lives")]
    state: Annotated[str, Field(...,description="state where the patient lives")]
    pincode: Annotated[str, Field(...,description="pincode of the area where the patient lives",json_schema_extra={"example": "110001"})]

class Patient(BaseModel):
    id: Annotated[str, Field(..., description="id of the patient", json_schema_extra={"example": "P001"})]
    name: Annotated[str, Field(..., description="name of the patient")]
    age: Annotated[int, Field(..., gt=0, lt=120, description="age of the patient")]
    gender: Annotated[Literal['male', 'female', 'other'], Field(..., description="gender of the patient")]
    height: Annotated[float, Field(..., gt=0, description="height of the patient should be in mtrs")]
    weight: Annotated[float, Field(..., gt=0, description="weight of the patient should be in kg")]
    BloodGroup: Annotated[Literal['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'], Field(..., description="blood group of the patient")]
    phone: Annotated[str, Field(..., description="phone number of the patient")]
    email: Annotated[EmailStr, Field(..., description="email address of the patient")]
    address: Annotated[Address, Field(..., description="address of the patient")]

    @computed_field
    def bmi(self)-> float:
        bmi = round(self.weight / (self.height ** 2),2)
        return bmi

app=FastAPI()

def load_data():
    with open('patients.json', 'r') as f:

        data =json.load(f)
    return data

def save_data(data):
    with open('patients.json', 'w') as f:
        json.dump(data, f)

@app.get('/')
def hello():
    return {"message": "Patient management system API"}

@app.get('/about')
def about():
    return {"message" : "A fully functional API for managing hospital patients."}

@app.get('/view')
def view():
    data = load_data()

    return data

@app.get('/patient/{patient_id}')
def view_patient(patient_id: str = Path(..., description="The ID of the patient in the system" , example="P001")):
      data =load_data()

      if patient_id in data:
        return data[patient_id]
      raise HTTPException(status_code=404, detail=f'Patient not found')

@app.get('/patients')
def search_patient(patient_name: str = Query(..., description="The name of the patient in the system" , example="rahul kumar")):
      data =load_data()

      for patient_id,patient in data.items():
        if patient['name'].lower() == patient_name.lower():
          return patient
      raise HTTPException(status_code=404, detail=f'Patient not found')

@app.get('/sort')
def sorted_patients(sort_by:str=Query(...,description="sort patients by age or height or weight "),order:str=Query(description="sort order: asc or desc")):
    if sort_by not in ['age','height','weight']:
        raise HTTPException(status_code=400,detail=f"Invalid sort_by value. Must be one of: 'age', 'height', 'weight'")
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail=f'Invalid order value. Must be one of: asc, desc')
    
    data = load_data()

    sorted_order=True if order == 'desc' else False

    sorted_data=sorted(data.values(),key=lambda x: x[sort_by],reverse=sorted_order)

    return sorted_data

@app.post('/create')
def create_patient(patient:Patient):

    data=load_data()
     
    if patient.id in data:
        raise HTTPException(status_code=400,detail="Patient with this ID already exists")
    
    data[patient.id]=patient.model_dump()   


    save_data(data)

    return JSONResponse(status_code=201,content={"message": "Patient created successfully"})

    