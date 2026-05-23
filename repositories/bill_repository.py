import os.path
from models.Bill import Bill, BillResponse, CreateBill
from typing import Optional,Dict,List
from datetime import datetime

class BillServiceError(Exception):
    pass

class BillRepository:

    def __init__(self):
        ## Project folder Path
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.file_path = os.path.join(base_dir,"data","bill.txt")
        self.__bills : Dict[str,BillResponse] = {}


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

    def create_bill(self,bill : CreateBill) -> BillResponse:

        bill_obj = BillResponse(
            bill_id=bill.bill_id,
            patient_id=bill.patient_id,
            consultation_fee=bill.consultation_fee,
            medicine_fee=bill.medicine_fee,
            room_fee=bill.room_fee,
            created_at=datetime.now().isoformat(),
            updated_at=datetime.now().isoformat()
        )

        self.__bills[bill.bill_id] = bill_obj
        return bill_obj

    def get_by_id(self,bill_id : str) -> Optional[BillResponse]:
        return self.__bills.get(bill_id)

    def get_all(self)-> List[BillResponse]:

        all_bills : List[BillResponse] = []

        for bill in self.__bills.values():
            all_bills.append(bill)

        if not all_bills:
            raise BillServiceError("No Bills Found")

        return all_bills

    def remove_bill(self, bill_id: str):

        if bill_id not in self.__bills:
            raise BillServiceError("Bill not found")

        del self.__bills[bill_id]

    def save_all(self,bills):
        with open(self.file_path,"w") as file:
            for bill in bills:
                file.write(bill.to_text()+"\n")






