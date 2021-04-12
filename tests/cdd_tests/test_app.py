import falcon
from falcon import testing
import pytest
from unittest.mock import MagicMock

from cdd.app import api

@pytest.fixture
def client():
    return testing.TestClient(api)
    