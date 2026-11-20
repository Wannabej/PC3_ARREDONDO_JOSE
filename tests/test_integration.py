from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_sumar_integracion():
    health_response = client.get("/health")
    sumar_response = client.get("/sumar", params={"a": 3, "b": 4})
    promedio_response = client.post("/promedio", json={"valores": [2, 4, 6]})

    assert health_response.status_code == 200
    assert health_response.json() == {"status": "ok"}
    assert sumar_response.status_code == 200
    assert sumar_response.json() == {"resultado": 7}
    assert promedio_response.status_code == 200
    assert promedio_response.json() == {"promedio": 4.0}
