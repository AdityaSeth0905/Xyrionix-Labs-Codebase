
import pytest
from fastapi.testclient import TestClient
from src.main import app

@pytest.fixture
def test_client():
    return TestClient(app)
