from abc import ABC,abstractmethod
from dataclasses import dataclass

@dataclass
class Person(ABC):
    person_id : str
    name : str
    age : int
    gender : str

    def display_basic_info(self,person):
            print(f"ID : {self.person_id}\n"
                  f"Name : {self.name}\n"
                  f"Age : {self.age}\n"
                  f"Gender : {self.gender}")

    @abstractmethod
    def display(self):
        pass
    @abstractmethod
    def to_text(self):
        pass
