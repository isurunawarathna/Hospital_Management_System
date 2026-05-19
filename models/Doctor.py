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
