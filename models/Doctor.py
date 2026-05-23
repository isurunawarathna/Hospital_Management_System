from models.Person import Person
from pydantic import Field
from typing import Optional

class Doctor(Person):
    specialization : str = Field(...,max_length=100,min_length=5,description="Doctor Specialization")

    def display(self):
        print(f"ID : {self.person_id}\n"
              f"Name : {self.name}\n"
              f"Age : {self.age}\n"
              f"Gender : {self.gender}\n"
              f"Specialization : {self.specialization}")

    def to_text(self):
        return f"{self.person_id},{self.name},{self.age},{self.gender},{self.specialization}"

    @staticmethod
    def from_text(line):
        data = line.strip().split(",")
        return Doctor(
            person_id=data[0],
            name=data[1],
            age=data[2],
            gender=data[3],
            specialization=data[4]
        )

class CreateDoctor(Doctor):
    pass

class DoctorResponse(Doctor):
    created_at : str
    updated_at : Optional[str] = None
