import os.path
from models.Appointments import Appointments, CreateAppointment,AppointmentResponse
from typing import Dict,Optional,List
from datetime import datetime

class AppointmentServiceError(Exception):
    pass

class AppointmentRepository:

    def __init__(self):
        ## Project folder Path
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.file_path = os.path.join(base_dir,"data","appointment.txt")
        self.__appointments : Dict[str,AppointmentResponse] = {}


    def find_all(self):
        appointments = []

        if not os.path.exists(self.file_path):
            return appointments
        with open(self.file_path,"r") as file:
            for line in file:
                if line.strip():
                    appointments.append(Appointments.from_text(line))
        return appointments

    def find_by_id(self,appointment_id):
        appointments = self.find_all()

        for appointment in appointments:
            if appointment_id == appointment.appointment_id:
                return appointment

        return None

    def add_appointment(self,appointment):

        appointments = self.find_all()
        appointments.append(appointment)
        self.save_all(appointments)

    def create_appointment(self,appointment : CreateAppointment) -> AppointmentResponse:

        appointment_obj = AppointmentResponse(
            appointment_id=appointment.appointment_id,
            patient_id=appointment.patient_id,
            doctor_id=appointment.doctor_id,
            date=appointment.date,
            time=appointment.time,
            created_at=datetime.now().isoformat(),
            updated_at=datetime.now().isoformat()
        )

        self.__appointments[appointment.appointment_id] = appointment_obj
        return appointment_obj

    def get_by_id(self,appointment_id : str) -> Optional[AppointmentResponse]:
        return self.__appointments.get(appointment_id)

    def get_all(self)-> List[AppointmentResponse]:

        all_appointments : List[AppointmentResponse] = []

        for appointment in self.__appointments.values():
            all_appointments.append(appointment)

        if not all_appointments:
            raise AppointmentServiceError("No Appointments Found")

        return all_appointments

    def remove_appointment(self, appointment_id: str):

        if appointment_id not in self.__appointments:
            raise AppointmentServiceError("Doctor not found")

        del self.__appointments[appointment_id]

    def save_all(self,appointments):
        with open(self.file_path,"w") as file:
            for appointment in appointments:
                file.write(appointment.to_text()+"\n")








