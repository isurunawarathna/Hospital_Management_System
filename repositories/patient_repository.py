import os.path
from models.Patient import Patient

class PatientRepository:

    def __init__(self):
        ## Project folder Path
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.file_path = os.path.join(base_dir,"data","patient.txt")

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
            if patient_id == patient["person_id"]:
                return patient
        return None

    def add(self,patient):

        patients = self.find_all()
        patients.append(patient)
        self.save_all(patients)

    def save_all(self,patients):
        with open(self.file_path,"w") as file:
            for patient in patients:
                file.write(patient.to_text()+"\n")






