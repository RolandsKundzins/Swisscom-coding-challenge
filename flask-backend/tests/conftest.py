import pytest
from api import app  # Import your Flask app

@pytest.fixture
def client():
    """Provides a test client for the Flask app."""
    with app.test_client() as client:
        yield client
