from fastapi import FastAPI
from Routers.patient_router import router as patient_router
from Routers.doctor_router import router as doctor_router
from Routers.appointment_router import router as appointment_router
from Routers.bill_router import router as bill_router

app = FastAPI(title="Sri Lankan Best Hospitality Management API")

app.include_router(patient_router)
app.include_router(doctor_router)
app.include_router(appointment_router)
app.include_router(bill_router)


