from typing import List

from repositories.appointment_repository import AppointmentServiceError
from services.appointment_service import AppointmentService
from models.Appointments import CreateAppointment, AppointmentResponse
from fastapi import HTTPException
from fastapi import APIRouter
from starlette import status

router = APIRouter(prefix="/appointment",tags=["appointment"])
appointment_service = AppointmentService()

@router.post("/",response_model=AppointmentResponse,status_code=status.HTTP_201_CREATED)
def create_appointment(appointment : CreateAppointment):
    try:
        return appointment_service.create_appointment(appointment=appointment)
    except AppointmentServiceError as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=str(e))

@router.get("/id/{appointment_id}",response_model=AppointmentResponse,status_code=status.HTTP_302_FOUND)
def get_appointment(appointment_id : str):
    try:
        return appointment_service.get_by_id(appointment_id=appointment_id)
    except AppointmentServiceError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )

@router.get("/all_doctors",response_model=List[AppointmentResponse],status_code=status.HTTP_302_FOUND)
def get_all_appointment():
    try:
        return appointment_service.get_all()
    except AppointmentServiceError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )
@router.delete("/delete/{appointment_id}",status_code=status.HTTP_204_NO_CONTENT)
def remove_appointment(appointment_id : str):
    try:
        return appointment_service.remove_appointment(appointment_id=appointment_id)
    except AppointmentServiceError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )




