import os.path
from models.Bill import Bill

class BillServiceError(Exception):
    pass

class BillRepository:

    def __init__(self):
        ## Project folder Path
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.file_path = os.path.join(base_dir,"data","bill.txt")


    def find_all(self):
        bills = []

        if not os.path.exists(self.file_path):
            return bills
        with open(self.file_path,"r") as file:
            for line in file:
                if line.strip():
                    bills.append(Bill.from_text(line))
        return bills

    def find_by_id(self,bill_id):
        bills = self.find_all()

        for bill in bills:
            if bill_id == bill.bill_id:
                return bill

        return None

    def add_bill(self,bill):

        bills = self.find_all()
        bills.append(bill)
        self.save_all(bills)

    def save_all(self,bills):
        with open(self.file_path,"w") as file:
            for bill in bills:
                file.write(bill.to_text()+"\n")






