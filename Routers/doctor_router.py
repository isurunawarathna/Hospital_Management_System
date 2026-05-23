from typing import List

from repositories.doctor_repository import DoctorServiceError
from services.doctor_service import DoctorService
from models.Doctor import DoctorResponse, CreateDoctor
from fastapi import HTTPException
from fastapi import APIRouter
from starlette import status

router = APIRouter(prefix="/doctor",tags=["doctor"])
doctor_service = DoctorService()

@router.post("/",response_model=DoctorResponse,status_code=status.HTTP_201_CREATED)
def create_doctor(doctor : CreateDoctor):
    try:
        return doctor_service.create_doctor(doctor=doctor)
    except DoctorServiceError as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=str(e))

@router.get("/id/{doctor_id}",response_model=DoctorResponse,status_code=status.HTTP_302_FOUND)
def get_doctor(doctor_id : str):
    try:
        return doctor_service.get_by_id(doctor_id=doctor_id)
    except DoctorServiceError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )

@router.get("/all_doctors",response_model=List[DoctorResponse],status_code=status.HTTP_302_FOUND)
def get_all_doctors():
    try:
        return doctor_service.get_all()
    except DoctorServiceError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )

@router.delete("/delete/{doctor_id}",status_code=status.HTTP_204_NO_CONTENT)
def remove_doctor(doctor_id : str):
    try:
        return doctor_service.remove_doctor(doctor_id=doctor_id)
    except DoctorServiceError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )





