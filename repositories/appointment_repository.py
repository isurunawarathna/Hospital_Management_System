import os.path
from models.Appointments import Appointments

class AppointmentServiceError(Exception):
    pass

class AppointmentRepository:

    def __init__(self):
        ## Project folder Path
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.file_path = os.path.join(base_dir,"data","appointment.txt")


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

    def save_all(self,appointments):
        with open(self.file_path,"w") as file:
            for appointment in appointments:
                file.write(appointment.to_text()+"\n")






