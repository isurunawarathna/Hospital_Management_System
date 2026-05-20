from repositories.bill_repository import BillRepository
from repositories.patient_repository import PatientRepository

class BillService:

    def __init__(self):
        self.bill_repository = BillRepository()
        self.patient_repository = PatientRepository()

    def add_bill(self, bill):

        existing_bill = self.bill_repository.find_by_id(bill.bill_id)

        if existing_bill:
            return "Bill ID already exist."

        patient = self.patient_repository.find_by_id(bill.patient_id)

        if patient is None:
            return "Patient does not exist"

        self.bill_repository.add_bill(bill)
        return "Bill Added successfully"

    def get_all_bill(self):
        return self.bill_repository.find_all()

    def get_bill_by_id(self, bill_id):
        return self.bill_repository.find_by_id(bill_id)

