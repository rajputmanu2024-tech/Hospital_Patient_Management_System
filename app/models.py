from typing import Annotated, Optional, Literal,Annotated
from pydantic import BaseModel, Field, EmailStr, computed_field




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
    address: Annotated[str, Field(..., description="address of the patient")]

    @computed_field
    def bmi(self)-> float:
        bmi = round(self.weight / (self.height ** 2),2)
        return bmi
    
class PatientUpdate(BaseModel):
    name: Annotated[Optional[str], Field(default=None, description="name of the patient")]
    age: Annotated[Optional[int], Field(default=None, gt=0, lt=120, description="age of the patient")]
    gender: Annotated[Optional[Literal['male', 'female', 'other']], Field(default=None, description="gender of the patient")]
    height: Annotated[Optional[float], Field(default=None, gt=0, description="height of the patient should be in mtrs")]
    weight: Annotated[Optional[float], Field(default=None, gt=0, description="weight of the patient should be in kg")]
    BloodGroup: Annotated[Optional[Literal['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']], Field(default=None, description="blood group of the patient")]
    phone: Annotated[Optional[str], Field(default=None, description="phone number of the patient")]
    email: Annotated[Optional[EmailStr], Field(default=None, description="email address of the patient")]
    address: Annotated[Optional[str], Field(default=None, description="address of the patient")]