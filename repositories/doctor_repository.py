import os.path
from models.Doctor import Doctor, CreateDoctor,DoctorResponse
from typing import Optional,Dict, List
from datetime import datetime


class DoctorServiceError(Exception):
    pass

class DoctorRepository:

    def __init__(self):
        ## Project folder Path
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.file_path = os.path.join(base_dir,"data","doctor.txt")
        self.__doctors : Dict[str,DoctorResponse] = {}

    def find_all(self):
        doctors = []

        if not os.path.exists(self.file_path):
            return doctors
        with open(self.file_path,"r") as file:
            for line in file:
                if line.strip():
                    doctors.append(Doctor.from_text(line))
        return doctors

    def find_by_id(self,doctor_id):
        doctors = self.find_all()

        for doctor in doctors:
            if doctor_id == doctor.person_id:
                return doctor

        return None

    def add_doctor(self,doctor):

        doctors = self.find_all()
        doctors.append(doctor)
        self.save_all(doctors)

    def create_doctor(self,doctor : CreateDoctor) -> DoctorResponse:

        doctor_obj = DoctorResponse(
            person_id=doctor.person_id,
            name=doctor.name,
            age=doctor.age,
            gender=doctor.gender,
            specialization=doctor.specialization,
            created_at=datetime.now().isoformat(),
            updated_at=datetime.now().isoformat()
        )

        self.__doctors[doctor.person_id] = doctor_obj
        return doctor_obj

    def get_by_id(self, doctor_id : str) -> Optional[DoctorResponse]:
        return self.__doctors.get(doctor_id)

    def get_all(self)-> List[DoctorResponse]:

        all_doctors : List[DoctorResponse] = []

        for doctor in self.__doctors.values():
            all_doctors.append(doctor)

        if not all_doctors:
            raise DoctorServiceError("No Doctors Found")

        return all_doctors

    def remove_doctor(self, doctor_id: str):

        if doctor_id not in self.__doctors:
            raise DoctorServiceError("Doctor not found")

        del self.__doctors[doctor_id]

    def save_all(self,doctors):
        with open(self.file_path,"w") as file:
            for doctor in doctors:
                file.write(doctor.to_text()+"\n")






