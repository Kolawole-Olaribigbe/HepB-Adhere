from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_ussd_route():
    response = client.post("/api/v1/ussd", json={"sessionId": "12345", "userInput": "1"})
    assert response.status_code == 200
    assert "responseMessage" in response.json()

def test_sms_route():
    response = client.post("/api/v1/sms", json={"to": "+1234567890", "message": "Test message"})
    assert response.status_code == 200
    assert "status" in response.json()

def test_patients_route():
    response = client.get("/api/v1/patients")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Expecting a list of patients

def test_create_patient_route():
    response = client.post("/api/v1/patients", json={"name": "John Doe", "phone": "+1234567890"})
    assert response.status_code == 201
    assert "id" in response.json()  # Expecting the created patient's ID in the response

def test_invalid_ussd_route():
    response = client.post("/api/v1/ussd", json={"sessionId": "12345", "userInput": "invalid"})
    assert response.status_code == 400  # Expecting a bad request for invalid input
    assert "error" in response.json()  # Expecting an error message in the response