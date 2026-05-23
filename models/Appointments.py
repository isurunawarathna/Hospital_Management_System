from pydantic import BaseModel,Field
from typing import Optional

class Appointments(BaseModel):
    appointment_id : str = Field(...,max_length=10,min_length=1,description="Appointment ID")
    patient_id : str = Field(...,max_length=10,min_length=1,description="Patient ID")
    doctor_id : str = Field(...,max_length=10,min_length=1,description="Doctor ID")
    date : str = Field(...,max_length=20,description="Appointment Date")
    time : str = Field(...,max_length=20,description="Appointment Time")

    def to_text(self):
        return f"{self.appointment_id},{self.patient_id},{self.doctor_id},{self.date},{self.time}"

    def display(self):
        print(f"Appointment ID : {self.appointment_id}\n"
              f"Patient ID : {self.patient_id}\n"
              f"Doctor ID : {self.doctor_id}\n"
              f"Date : {self.date}\n"
              f"Time : {self.time}")

    @staticmethod
    def from_text(line):
        data = line.strip().split(",")
        return Appointments(
            appointment_id=data[0],
            patient_id=data[1],
            doctor_id=data[2],
            date=data[3],
            time=data[4]
        )

class CreateAppointment(Appointments):
    pass

class AppointmentResponse(Appointments):
    created_at : str
    updated_at : Optional[str] = None