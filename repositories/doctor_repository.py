import os.path
from models.Doctor import Doctor

class DoctorRepository:

    def __init__(self):
        ## Project folder Path
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.file_path = os.path.join(base_dir,"data","doctor.txt")
        self.save_all()

    def find_all(self):
        doctors = []

        if not os.path.exists(self.file_path):
            return doctors
        with open(self.file_path,"r") as file:
            for line in file:
                if line.strip():
                    doctors.append(Doctor.from_text(line))
        return doctors

    def add(self,doctor):

        doctors = self.find_all()
        doctors.append(doctor)

    def save_all(self,doctors):
        with open(self.file_path,"w") as file:
            for doctor in doctors:
                file.write(doctor.to_text()+"\n")






