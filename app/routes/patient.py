from fastapi import FastAPI,APIRouter, Path , HTTPException,Query
from fastapi.responses import JSONResponse
from app.models import Patient,PatientUpdate
from app.database import load_data,save_data

router=APIRouter()


@router.get('/')
def hello():
    return {"message": "Patient management system API"}

@router.get('/about')
def about():
    return {"message" : "A fully functional API for managing hospital patients."}

@router.get('/view')
def view():
    data = load_data()

    return data

@router.get('/patient/{patient_id}')
def view_patient(patient_id: str = Path(..., description="The ID of the patient in the system" , example="P001")):
      data =load_data()

      if patient_id in data:
        return data[patient_id]
      raise HTTPException(status_code=404, detail=f'Patient not found')

@router.get('/patients')
def search_patient(patient_name: str = Query(..., description="The name of the patient in the system" , example="rahul kumar")):
      data =load_data()

      for patient_id,patient in data.items():
        if patient['name'].lower() == patient_name.lower():
          return patient
      raise HTTPException(status_code=404, detail=f'Patient not found')

@router.get('/sort')
def sorted_patients(sort_by:str=Query(...,description="sort patients by age or height or weight "),order:str=Query(description="sort order: asc or desc")):
    if sort_by not in ['age','height','weight']:
        raise HTTPException(status_code=400,detail=f"Invalid sort_by value. Must be one of: 'age', 'height', 'weight'")
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail=f'Invalid order value. Must be one of: asc, desc')
    
    data = load_data()

    sorted_order=True if order == 'desc' else False

    sorted_data=sorted(data.values(),key=lambda x: x[sort_by],reverse=sorted_order)

    return sorted_data

@router.post('/create')
def create_patient(patient:Patient):

    data=load_data()
     
    if patient.id in data:
        raise HTTPException(status_code=400,detail="Patient with this ID already exists")
    
    data[patient.id]=patient.model_dump()   


    save_data(data)

    return JSONResponse(status_code=200,content={"message": "Patient created successfully", "patient": patient.model_dump()},)

    
@router.put('/edit/{patient_id}')
def update_patient(patient_id: str, patient_update: PatientUpdate):
    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    existing_patient = data[patient_id]
    updated_patient = patient_update.model_dump(exclude_unset=True)


    # Update the patient's information
    for key, value in updated_patient.items():
        existing_patient[key] = value

    existing_patient['id']= patient_id  # Ensure the ID remains unchanged

    patient_pydantic_obj = Patient(**existing_patient)

    existing_patient=patient_pydantic_obj.model_dump()

    data[patient_id] = existing_patient

    save_data(data)
    return {"message": "Patient updated successfully", "patient": data[patient_id]}


@router.delete('/delete/{patient_id}')
def deletePatient(patient_id:str=Path(description="enter the patient id to delete" , json_schema_extra={"example":"P001"})):
    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code= 404,detail="patient not found")
    delete_patient=data.pop(patient_id)

    save_data(data)
    return JSONResponse(status_code=201,content={"message": "Patient deleted successfully"})