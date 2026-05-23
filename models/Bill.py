from pydantic import BaseModel,Field
from typing import Optional

class Bill(BaseModel):
    bill_id : str = Field(...,max_length=10,min_length=1,description="Bill ID")
    patient_id : str = Field(...,max_length=10,min_length=1,description="Patient ID")
    consultation_fee : float = Field(...,le=10000,description="Doctor Consultation Fee")
    medicine_fee : float = Field(...,le=10000,description="Doctor Consultation Fee")
    room_fee : float = Field(...,le=10000,description="Doctor Consultation Fee")

    def get_total(self):
        return self.consultation_fee + self.medicine_fee + self.room_fee

    def to_text(self):
        return f"{self.bill_id},{self.patient_id},{self.consultation_fee},{self.medicine_fee},{self.room_fee}"

    def display(self):
        print(f"Bill ID : {self.bill_id}\n"
              f"Patient ID : {self.patient_id}\n"
              f"Consultation Fee : {self.consultation_fee}\n"
              f"Medicine Fee : {self.medicine_fee}\n"
              f"Room Fee : {self.room_fee}")

    @staticmethod
    def from_text(line):
        data = line.strip().split(",")
        return Bill(
            bill_id=data[0],
            patient_id=data[1],
            consultation_fee=data[2],
            medicine_fee=data[3],
            room_fee=data[4]
        )

class CreateBill(Bill):
    pass

class BillResponse(Bill):
    created_at : str
    updated_at : Optional[str] = None
