from services.appointment_service import AppointmentService
from services.doctor_service import DoctorService
from services.patient_service import PatientService
from services.bill_service import BillService
from models.Patient import Patient
from models.Doctor import Doctor
from models.Appointments import Appointments
from models.Bill import  Bill

patient_service = PatientService()
doctor_service = DoctorService()
appointment_service = AppointmentService()
bill_service = BillService()

while True:

    print("\n============Hospital Management=====================\n\n"
          "1.Add Patient\n"
          "2.View All Patient\n"
          "3.View Patient by Id\n"
          "4.Add Doctor\n"
          "5.View All Doctors\n"
          "6.View Doctor by Id\n"
          "7.Add Appointment\n"
          "8.View All Appointment\n"
          "9.View Appointment by Id\n"
          "10.Add Bill\n"
          "11.View All Bills\n"
          "12.View Bill by Id\n"
          "13.Exit\n")

    user_input = input("Enter Your Choice : ").strip()

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
        print(f"Patient Added to the System Successfully. Patient ID - {patient_id}")

    elif user_input == "2":

        print("\n====All Patients=======")

        patients = patient_service.get_all_patient()

        if not patients:
            print("No Patients Found")

        for patient in patients:
            print("----------------------\n")
            patient.display()
            print("----------------------\n")

    elif user_input == "3":

        print("\n====Patients by ID=======")

        patient_id = input("Enter Patient Id : ").strip()

        patient = patient_service.get_patient_by_id(patient_id=patient_id)

        if not patient:
            print("No Patient Found")

        patient.display()

    elif user_input == "4":

        print("\n====Add Doctor=======")

        doctor_id = input("Enter Doctor Id : ").strip()
        name = input("Enter Doctor Name : ").strip()
        age = input("Enter age : ").strip()
        gender = input("Enter Gender : ").strip()
        specialization = input("Enter Specialization : ").strip()

        doctor = Doctor(
            person_id=doctor_id,
            name=name,
            age=int(age),
            gender=gender,
            specialization=specialization
        )

        doctor_service.add_doctor(doctor)
        print(f"Doctor Added to the System Successfully. Doctor ID - {doctor_id}")

    elif user_input == "5":

        print("\n====View All Doctor=======")

        doctors = doctor_service.get_all_doctor()

        if not doctors:
            print("No Doctors Found")

        for doctor in doctors:

            print("----------------------\n")
            doctor.display()
            print("----------------------\n")

    elif user_input == "6":

        print("\n====View Doctor by Id=======")

        doctor_id = input("Enter Doctor Id : ").strip()

        doctor = doctor_service.get_doctor_by_id(doctor_id=doctor_id)

        if not doctor:
            print("Not Found Doctor")

        doctor.display()


    elif user_input == "7":

        print("\n====Add Appointment=======")

        appointment_id =  input("Enter Appointment Id : ").strip()
        patient_id = input("Enter Patient Id : ").strip()
        doctor_id =  input("Enter Doctor Id : ").strip()
        date = input("Enter Date : ").strip()
        time = input("Enter Time : ").strip()

        appointment = Appointments(
            appointment_id=appointment_id,
            patient_id=patient_id,
            doctor_id=doctor_id,
            date=date,
            time=time
        )

        appointment_service.add_appointment(appointment)
        print(f"Appointment Added to the System Successfully. Appointment ID - {appointment_id}")

    elif user_input == "8":

        print("\n====View All Appointment=======")

        appointments = appointment_service.get_all_appointment()

        if not appointments:
            print("No Appointment Found")

        for appointment in appointments:
            print("----------------------\n")
            appointment.display()
            print("----------------------\n")


    elif user_input == "9":

        print("\n====View Appointment by Id=======")

        appointment_id = input("Enter Appointment Id : ").strip()

        appointment = appointment_service.get_appointment_by_id(appointment_id=appointment_id)

        if not appointment:
            print("Not Found Appointment")

        appointment.display()

    elif user_input == "10":

        bill_id = input("Enter Bill Id : ").strip()
        patient_id = input("Enter Patient Id : ").strip()
        consultation_fee = input("Enter Consultation Fee : ").strip()
        medicine_fee = input("Enter Medicine Fee : ").strip()
        room_fee = input("Enter Room Fee : ").strip()

        bill = Bill(
             bill_id=bill_id,
             patient_id=patient_id,
             consultation_fee=consultation_fee,
             medicine_fee=medicine_fee,
             room_fee=room_fee
        )

        bill_service.add_bill(bill)
        print(f"Bill Added to the System Successfully. Bill ID - {bill_id}")

    elif user_input == "11":

        print("\n====All Bills=======")

        bills = bill_service.get_all_bill()

        if not bills:
            print("No Bills Found")

        for bill in bills:
            print("----------------------\n")
            bill.display()
            print("----------------------\n")

    elif user_input == "12":

        print("\n====View Bill by Id=======")

        bill_id = input("Enter Bill Id : ").strip()

        bill = bill_service.get_bill_by_id(bill_id=bill_id)

        if not bill:
            print("Not Found Doctor")

        bill.display()

    elif user_input == "13":
        break

    else:
        print("Invalid Choice.Please try again")














