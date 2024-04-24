"""Test FastAPI routes"""

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_root():
    response = client.get("/feature_flag/feature")
    assert response.json() == {'message': 'hello'}
