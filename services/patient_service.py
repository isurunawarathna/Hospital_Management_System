from repositories.patient_repository import PatientRepository

class PatientService:

    def __init__(self):
        self.patient_repository = PatientRepository()

    def add_patient(self, patient):

        existing_patient = self.patient_repository.find_by_id(patient.person_id)

        if existing_patient:
            print("Patient Id already Exits")

        self.patient_repository.add(patient)
        return "Patient Added Successfully"

    def get_all_patient(self):
        return self.patient_repository.find_all()

    def get_patient_by_id(self,patient_id):
        return self.patient_repository.find_by_id(patient_id)
