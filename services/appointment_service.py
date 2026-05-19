from repositories.appointment_repository import AppointmentRepository
from repositories.doctor_repository import DoctorRepository
from repositories.patient_repository import PatientRepository


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

        self.appointment_repository.add(appointment)
        return "Appointment Added successfully"

    def get_all_appointment(self):
        return self.appointment_repository.find_all()

    def get_all_patient_by_id(self, appointment_id):
        return self.appointment_repository.find_by_id(appointment_id)

