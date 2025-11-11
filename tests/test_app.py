import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    # Prüfen, dass der Haupttitel auf der Startseite vorhanden ist
    assert b"Foto WebApp" in response.data
    # Optional: Prüfen, dass der Button da ist
    assert b"Foto aufnehmen" in response.data
