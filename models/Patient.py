from pydantic import Field
from models.Person import Person
from typing import Optional

class Patient(Person):
    disease: str = Field(...,max_length=100, min_length=5,description="Patient Disease")

    def display(self):
        print(f"ID : {self.person_id}\n"
              f"Name : {self.name}\n"
              f"Age : {self.age}\n"
              f"Gender : {self.gender}\n"
              f"Disease : {self.disease}")

    def to_text(self):
       return f"{self.person_id},{self.name},{self.age},{self.gender},{self.disease}"

    @staticmethod
    def from_text(line):
        data = line.strip().split(",")
        return Patient(
            person_id=data[0],
            name=data[1],
            age=data[2],
            gender=data[3],
            disease=data[4]
        )

class CreatePatient(Patient):
    pass

class PatientResponse(Patient):
    created_at : str
    updated_at : Optional[str] = None