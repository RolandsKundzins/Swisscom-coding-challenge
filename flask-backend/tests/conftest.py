import pytest

# Ignore deprecation warnings from Pydantic, which is part of acryl-datahub dependency
# As of latest current version 0.15.0.1, the issue still persists
# If package is updated, this workaround might not be needed
import warnings
try:
    from pydantic import PydanticDeprecatedSince20
except ImportError:
    PydanticDeprecatedSince20 = DeprecationWarning

warnings.filterwarnings(
    "ignore",
    message="Support for class-based `config` is deprecated.*",
    category=PydanticDeprecatedSince20,
)


from api import app  # Import your Flask app

@pytest.fixture
def client():
    """Provides a test client for the Flask app."""
    with app.test_client() as client:
        yield client
