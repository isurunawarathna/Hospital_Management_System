from repositories.appointment_repository import AppointmentServiceError
from services.appointment_service import AppointmentService
from fastapi import HTTPException
from fastapi import APIRouter
from starlette import status

router = APIRouter(prefix="/appointment",tags=["appointment"])
appointment_service = AppointmentService()

@router.post("/",status_code=status.HTTP_201_CREATED)
def add_appointment(appointment):
    try:
        return appointment_service.add_appointment(appointment=appointment)
    except AppointmentServiceError as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=str(e))

@router.get("/id/{appointment_id}")
def get_appointment(appointment_id):
    try:
        return appointment_service.get_appointment_by_id(appointment_id=appointment_id)
    except AppointmentServiceError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.get("/all_doctors")
def get_all_appointment():
    try:
        appointments = appointment_service.get_all_appointment()
        return appointments
    except AppointmentServiceError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )





