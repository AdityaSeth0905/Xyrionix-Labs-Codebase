
import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "Server is healthy"}

def test_send_email_endpoint():
    email_data = {
        "to": "recipient@example.com",
        "subject": "Test Email",
        "body": "This is a test email"
    }
    
    response = client.post("/send-email", json=email_data)
    assert response.status_code == 200
    assert response.json() == {"status": "Email queued successfully"}
