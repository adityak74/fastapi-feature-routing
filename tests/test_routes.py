"""Test FastAPI routes"""

from fastapi.testclient import TestClient
from ff_routing_fastapi.main import app

client = TestClient(app)


def test_root():
    response = client.get("/feature_flag/feature")
    assert response.json() == {'message': 'hello'}
