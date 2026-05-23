from typing import Optional, List
from repositories.appointment_repository import AppointmentRepository
from repositories.doctor_repository import DoctorRepository
from repositories.patient_repository import PatientRepository
from models.Appointments import CreateAppointment, AppointmentResponse

class AppointmentService:

    def __init__(self):
        self.appointment_repository = AppointmentRepository()
        self.patient_repository = PatientRepository()
        self.doctor_repository = DoctorRepository()

    def add_appointment(self, appointment):

        existing_appointment = self.appointment_repository.find_by_id(appointment.appointment_id)

        if existing_appointment:
            return "Appointment ID already exist."

        patient = self.patient_repository.find_by_id(appointment.patient_id)

        if patient is None:
            return "Patient does not exist"

        doctor = self.doctor_repository.find_by_id(appointment.doctor_id)

        if doctor is None:
            return "doctor does not exist"

        self.appointment_repository.add_appointment(appointment)
        return "Appointment Added successfully"

    def get_all_appointment(self):
        return self.appointment_repository.find_all()

    def get_appointment_by_id(self, appointment_id):
        return self.appointment_repository.find_by_id(appointment_id)

    def create_appointment(self, appointment : CreateAppointment) -> AppointmentResponse:
        return self.appointment_repository.create_appointment(appointment=appointment)

    def get_by_id(self, appointment_id : str) -> Optional[AppointmentResponse]:
        return self.appointment_repository.get_by_id(appointment_id=appointment_id)

    def get_all(self) -> List[AppointmentResponse]:
        return self.appointment_repository.get_all()

    def remove_appointment(self, appointment_id):
        return self.appointment_repository.remove_appointment(appointment_id=appointment_id)
