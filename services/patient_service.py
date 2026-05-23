from typing import Optional, List
from repositories.patient_repository import PatientRepository
from models.Patient import  CreatePatient, PatientResponse

class PatientService:

    def __init__(self):
        self.patient_repository = PatientRepository()

    def add_patient(self, patient):

        existing_patient = self.patient_repository.find_by_id(patient.person_id)

        if existing_patient:
            print("Patient Id already Exits")

        self.patient_repository.add_patient(patient)
        return "Patient Added Successfully"

    def get_all_patient(self):
        return self.patient_repository.find_all()

    def get_patient_by_id(self,patient_id):
        return self.patient_repository.find_by_id(patient_id)

    def create_patient(self, patient : CreatePatient) -> PatientResponse:
        return self.patient_repository.create_patient(patient=patient)

    def get_by_id(self, patient_id : str) -> Optional[PatientResponse]:
        return self.patient_repository.get_by_id(patient_id=patient_id)

    def get_all(self) -> List[PatientResponse]:
        return self.patient_repository.get_all()

    def remove_patient(self, patient_id):
        return self.patient_repository.remove_patient(patient_id=patient_id)

