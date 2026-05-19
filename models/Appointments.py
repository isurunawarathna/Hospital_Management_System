from dataclasses import dataclass

@dataclass
class Appointments:

    appointment_id : str
    patient_id : str
    doctor_id : str
    date : str
    time : str

    def to_text(self):
        return f"{self.appointment_id},{self.patient_id},{self.doctor_id},{self.date},{self.time}"

    def display(self):
        print(f"Appointment ID : {self.appointment_id}\n"
              f"Patient ID : {self.patient_id}\n"
              f"Doctor ID : {self.doctor_id}\n"
              f"Date : {self.date}\n"
              f"Time : {self.time}")
