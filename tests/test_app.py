import os
import sys
import pytest

# Dodaj katalog nadrzędny do sys.path, aby uzyskać dostęp do modułu app.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importuj aplikację Flask
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello_world(client):
    response = client.get('/')
    assert response.data == b'hello, world!'
    assert response.status_code == 200
