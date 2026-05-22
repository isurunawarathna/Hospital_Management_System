from repositories.doctor_repository import DoctorServiceError
from services.doctor_service import DoctorService
from fastapi import HTTPException
from fastapi import APIRouter
from starlette import status

router = APIRouter(prefix="/doctor",tags=["doctor"])
doctor_service = DoctorService()

@router.post("/",status_code=status.HTTP_201_CREATED)
def add_doctor(doctor):
    try:
        return doctor_service.add_doctor(doctor=doctor)
    except DoctorServiceError as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=str(e))

@router.get("/id/{doctor_id}")
def get_doctor(doctor_id):
    try:
        return doctor_service.get_doctor_by_id(doctor_id=doctor_id)
    except DoctorServiceError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.get("/all_doctors")
def get_all_doctors():
    try:
        doctors = doctor_service.get_all_doctor()
        return doctors
    except DoctorServiceError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )





