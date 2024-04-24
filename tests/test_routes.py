"""Test FastAPI routes"""

from fastapi.testclient import TestClient
from ff_routing_fastapi.main import app

client = TestClient(app)


def test_feature():
    response = client.get("/feature_flag/feature")
    assert response.json() == {'message': 'hello'}


def test_feature_flag():
    response = client.get("/feature_flag/feature_async")
    assert response.json() == {'message': 'hello'}
