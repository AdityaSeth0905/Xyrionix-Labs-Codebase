
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

api_router = APIRouter()

class EmailRequest(BaseModel):
    to: str
    subject: str
    body: str

@api_router.post("/send-email")
async def send_email(email: EmailRequest):
    # Placeholder for email sending logic
    return {"status": "Email queued successfully"}

@api_router.get("/health")
async def health_check():
    return {"status": "Server is healthy"}
