from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_promedio_lista_valida():
    response = client.post("/promedio", json={"valores": [2, 4, 6]})

    assert response.status_code == 200
    assert response.json() == {"promedio": 4.0}


def test_promedio_lista_vacia():
    response = client.post("/promedio", json={"valores": []})

    assert response.status_code == 400
    assert response.json() == {"detail": "Lista vacía"}
