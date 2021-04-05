import falcon
from falcon import testing
import pytest
from unittest.mock import MagicMock

from cdd.app import api

@pytest.fixture
def client():
    return testing.TestClient(api)

def test_get_tickets(client):
    doc = {
        "id": 1,
        "date": "2020-03-12",
        "base": "PE - CARUARU",
        "country_state": "PE",
        "consumption": 1            
    }

    response = client.simulate_get('/tickets')
    result_doc = response.json[0]

    assert result_doc == doc
    assert response.status == falcon.HTTP_OK

def test_get_all_tickets_from_a_base(client):
    doc = [
        {
            "id": 101,
            "date": "2021-03-09",
            "base": "SC - BLUMENAU",
            "country_state": "SC",
            "consumption": 1
        },
        {
            "id": 102,
            "date": "2021-03-09",
            "base": "SC - BLUMENAU",
            "country_state": "SC",
            "consumption": 1
        }
    ]

    response = client.simulate_get('/tickets/SC - BLUMENAU')
    result_doc = response.json

    assert result_doc == doc
    assert response.status == falcon.HTTP_OK

def test_if_average_value_of_tickets_of_a_base(client):
    doc = {
        "ticket_base": "SC - BLUMENAU",
        "average": 2
    }

    response = client.simulate_get('/tickets/SC - BLUMENAU/average')
    result_doc = response.json

    assert result_doc == doc
    assert response.status == falcon.HTTP_OK

def test_if_average_value_of_tickets_of_a_base(client):
    doc = {
        "ticket_base": "SC - BLUMENAU",
        "average": 2
    }

    response = client.simulate_get('/tickets/SC - BLUMENAU/average')
    result_doc = response.json

    assert result_doc == doc
    assert response.status == falcon.HTTP_OK
