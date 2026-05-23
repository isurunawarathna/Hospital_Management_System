from typing import List

from repositories.bill_repository import BillServiceError
from services.bill_service import BillService
from models.Bill import CreateBill,BillResponse
from fastapi import HTTPException
from fastapi import APIRouter
from starlette import status

router = APIRouter(prefix="/bill",tags=["bill"])
bill_service = BillService()

@router.post("/",response_model=BillResponse,status_code=status.HTTP_201_CREATED)
def create_bill(bill : CreateBill):
    try:
        return bill_service.create_bill(bill=bill)
    except BillServiceError as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=str(e))

@router.get("/id/{bill_id}",response_model=BillResponse,status_code=status.HTTP_302_FOUND)
def get_bill(bill_id : str):
    try:
        return bill_service.get_by_id(bill_id=bill_id)
    except BillServiceError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )

@router.get("/all_bills",response_model=List[BillResponse],status_code=status.HTTP_302_FOUND)
def get_all_bill():
    try:
        return bill_service.get_all()
    except BillServiceError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )

@router.delete("/delete/{bill_id}",status_code=status.HTTP_204_NO_CONTENT)
def remove_bill(bill_id : str):
    try:
        return bill_service.remove_bill(bill_id=bill_id)
    except BillServiceError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )





