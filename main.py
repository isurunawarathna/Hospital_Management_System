from services.appointment_service import AppointmentService
from services.doctor_service import DoctorService
from services.patient_service import PatientService
from models.Patient import Patient

patient_service = PatientService()
doctor_service = DoctorService()
appointment_service = AppointmentService()

while True:
    print("\n===Hospital Management====")
    user_input = input("1.Add Patient\n"
                       "2.View All Patient\n"
                       "3.Add Doctor\n"
                       "4.View All Doctors"
                       "5.View Doctor by Id"
                       "6.")

    if user_input == "1":
        patient_id = input("Enter Patient Id : ").strip()
        name = input("Enter Patient Name : ").strip()
        age = input("Enter age: ").strip()
        gender = input("Enter Gender: ").strip()

        disease = input("Enter Disease: ").strip()

        patient = Patient(
            person_id=patient_id,
            name=name,
            age=int(age),
            gender=gender,
            disease=disease
        )

        patient_service.add_patient(patient)

    elif user_input == "2":

        print("====All Patients=======")

        patients = patient_service.get_all_patient()

        if not patients:
            print("No Patient Found")

        for patient in patients:
            print("----------------------\n")
            patient.display()

