from repositories.patient_repository import PatientServiceError
from services.patient_service import PatientService
from fastapi import APIRouter
from fastapi import HTTPException
from starlette import status

router = APIRouter(prefix="/patient",tags=["patient"])
patient_service = PatientService()

@router.post("/",status_code=status.HTTP_201_CREATED)
def add_patient(patient):
    try:
        return patient_service.add_patient(patient=patient)
    except PatientServiceError as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=str(e))

@router.get("/id/{patient_id}")
def get_patient(patient_id):
    try:
        return patient_service.get_patient_by_id(patient_id=patient_id)
    except PatientServiceError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.get("/all_patients")
def get_all_patients():
    try:
        patients = patient_service.get_all_patient()
        return patients
    except PatientServiceError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )





