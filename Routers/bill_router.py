from repositories.bill_repository import BillServiceError
from services.bill_service import BillService
from fastapi import HTTPException
from fastapi import APIRouter
from starlette import status

router = APIRouter(prefix="/bill",tags=["bill"])
bill_service = BillService()

@router.post("/",status_code=status.HTTP_201_CREATED)
def add_bill(bill):
    try:
        return bill_service.add_bill(bill=bill)
    except BillServiceError as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=str(e))

@router.get("/id/{bill_id}")
def get_bill(bill_id):
    try:
        return bill_service.get_bill_by_id(bill_id=bill_id)
    except BillServiceError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.get("/all_bills")
def get_all_bill():
    try:
        bills = bill_service.get_all_bill()
        return bills
    except BillServiceError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )





