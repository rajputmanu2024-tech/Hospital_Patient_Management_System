from fastapi import FastAPI,APIRouter

from app.routes import patient

app = FastAPI()

app.include_router(patient.router)