from fastapi.testclient import TestClient

from core.main import app


def test_returns_json():
    client = TestClient(app)
    response = client.get('/')

    assert response.status_code == 200
    assert response.headers['content-type'] == 'application/json'
    assert response.json() == {'message': 'Hello World'}
