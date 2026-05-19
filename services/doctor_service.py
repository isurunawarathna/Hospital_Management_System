from repositories.doctor_repository import DoctorRepository


class DoctorService:

    def __init__(self):
        self.doctor_repository = DoctorRepository()

    def add_doctor(self, doctor):
        existing_doctor = self.doctor_repository.find_by_id(doctor.person_id)

        if existing_doctor:
            print("Doctor Id already Exits")

        self.doctor_repository.add(doctor)
        return "Doctor Added Successfully"

    def get_all_patient(self):
        return self.doctor_repository.find_all()

    def get_all_patient_by_id(self, doctor_id):
        return self.doctor_repository.find_by_id(doctor_id)
