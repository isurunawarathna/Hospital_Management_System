from abc import ABC,abstractmethod
from pydantic import BaseModel, Field

class Person(BaseModel,ABC):
    person_id : str = Field(...,max_length=10,min_length=1,description="Person ID")
    name : str = Field(...,max_length=100,min_length=1,description="Person Name")
    age : int = Field(...,ge=10,description="Person Age")
    gender : str = Field(...,max_length=10,min_length=4,description="Person Gender")

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
