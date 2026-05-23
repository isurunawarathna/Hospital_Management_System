from typing import Optional,List
from repositories.doctor_repository import DoctorRepository
from models.Doctor import DoctorResponse,CreateDoctor

class DoctorService:

    def __init__(self):
        self.doctor_repository = DoctorRepository()

    def add_doctor(self, doctor):
        existing_doctor = self.doctor_repository.find_by_id(doctor.person_id)

        if existing_doctor:
            print("Doctor Id already Exits")

        self.doctor_repository.add_doctor(doctor)
        return "Doctor Added Successfully"

    def get_all_doctor(self):
        return self.doctor_repository.find_all()

    def get_doctor_by_id(self, doctor_id):
        return self.doctor_repository.find_by_id(doctor_id)

    def create_doctor(self, doctor : CreateDoctor) -> DoctorResponse:
        return self.doctor_repository.create_doctor(doctor=doctor)

    def get_by_id(self, doctor_id : str) -> Optional[DoctorResponse]:
        return self.doctor_repository.get_by_id(doctor_id=doctor_id)

    def get_all(self) -> List[DoctorResponse]:
        return self.doctor_repository.get_all()

    def remove_doctor(self, doctor_id):
        return self.doctor_repository.remove_doctor(doctor_id=doctor_id)

