import falcon
from falcon import testing
import pytest

from cdd.app import api

@pytest.fixture
def client():
    return testing.TestClient(api)

def test_get_stocks(client):
    doc = {
            'id' : 1,
            'base': 'AC - RIO BRANCO',
            'value': 379
    }

    response = client.simulate_get('/stocks')
    result_doc = response.json[0]

    assert result_doc == doc
    assert response.status == falcon.HTTP_OK