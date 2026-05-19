from models.Person import Person
from dataclasses import dataclass

@dataclass
class Doctor(Person):
    specialization : str

    def display(self):
        print(f"ID : {self.person_id}\n"
              f"Name : {self.name}\n"
              f"Age : {self.age}\n"
              f"Gender : {self.gender}\n"
              f"Disease : {self.disease}\n"
              f"Specialization : {self.specialization}")

    def to_text(self):
        return f"{self.person_id},{self.name},{self.age},{self.gender},{self.disease},{self.specialization}"

