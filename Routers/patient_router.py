from typing import List
from repositories.patient_repository import PatientServiceError
from services.patient_service import PatientService
from models.Patient import CreatePatient,PatientResponse
from fastapi import APIRouter
from fastapi import HTTPException
from starlette import status

router = APIRouter(prefix="/patient",tags=["patient"])
patient_service = PatientService()

@router.post("/",response_model=PatientResponse,status_code=status.HTTP_201_CREATED)
def create_patient(patient : CreatePatient):
    try:
        return patient_service.create_patient(patient=patient)
    except PatientServiceError as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=str(e))

@router.get("/id/{patient_id}",response_model=PatientResponse,status_code=status.HTTP_302_FOUND)
def get_patient(patient_id : str):
    try:
        return patient_service.get_by_id(patient_id=patient_id)
    except PatientServiceError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )

@router.get("/all_patients",response_model=List[PatientResponse],status_code=status.HTTP_302_FOUND)
def get_all_patients():
    try:
        return patient_service.get_all()
    except PatientServiceError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )
@router.delete("/delete/{patient_id}",status_code=status.HTTP_204_NO_CONTENT)
def remove_patient(patient_id : str):
    try:
        return patient_service.remove_patient(patient_id=patient_id)
    except PatientServiceError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )




