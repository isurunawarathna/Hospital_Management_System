import os.path
from models.Patient import Patient, CreatePatient, PatientResponse
from typing import Dict,Optional,List
from datetime import datetime

class PatientServiceError(Exception):
    pass

class PatientRepository:

    def __init__(self):
        ## Project folder Path
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.file_path = os.path.join(base_dir,"data","patient.txt")
        self.__patients : Dict[str,PatientResponse] = {}

    def find_all(self):
        patients = []

        if not os.path.exists(self.file_path):
            return patients
        with open(self.file_path,"r") as file:
            for line in file:
                if line.strip():
                    patients.append(Patient.from_text(line))
        return patients

    def find_by_id(self,patient_id):
        patients = self.find_all()

        for patient in patients:
            if patient_id == patient.person_id:
                return patient
        return None

    def add_patient(self,patient):

        patients = self.find_all()
        patients.append(patient)
        self.save_all(patients)

    def create_patient(self, patient : CreatePatient) -> PatientResponse:

        patient_obj = PatientResponse(
            person_id=patient.person_id,
            name=patient.name,
            age=patient.age,
            gender=patient.gender,
            disease=patient.disease,
            created_at=datetime.now().isoformat(),
            updated_at=datetime.now().isoformat()
        )

        self.__patients[patient.person_id] = patient_obj
        return patient_obj

    def get_by_id(self,patient_id : str) -> Optional[PatientResponse]:
        if patient_id not in self.__patients:
            return None
        return self.__patients.get(patient_id)

    def get_all(self)-> List[PatientResponse]:

        all_patients : List[PatientResponse] = []

        for patient in self.__patients.values():
            all_patients.append(patient)

        if not all_patients:
            raise PatientServiceError("No Patients Found")

        return all_patients

    def remove_patient(self, patient_id: str):

        if patient_id not in self.__patients:
            raise PatientServiceError("Patient not found")

        del self.__patients[patient_id]

    def save_all(self,patients):
        with open(self.file_path,"w") as file:
            for patient in patients:
                file.write(patient.to_text()+"\n")






