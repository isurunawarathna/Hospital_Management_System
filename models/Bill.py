from dataclasses import dataclass

@dataclass
class Bill:
    bill_id : str
    patient_id : str
    consultation_fee : str
    medicine_fee : str
    room_fee : str

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