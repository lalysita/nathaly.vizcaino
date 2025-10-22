# test_app.py
import pytest
from app import app, sumar

# 1. Prueba Unitaria
def test_sumar():
    """Prueba que la función sumar funciona correctamente."""
    assert sumar(2, 3) == 5

# 2. Prueba de Integración
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hola_mundo_endpoint(client):
    """Prueba que el endpoint principal '/' responde correctamente."""
    response = client.get('/')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Hola, Mundo!'