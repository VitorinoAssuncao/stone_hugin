import falcon
from falcon import testing
import pytest
from unittest.mock import MagicMock

from cdd.app import api

@pytest.fixture
def client():
    return testing.TestClient(api)

def test_get_stocks(client):
    doc = {
        "id": 2,
        "base": "AL - MACEIO",
        "value": 98
    }

    response = client.simulate_get('/stocks')
    result_doc = response.json[0]

    assert result_doc == doc
    assert response.status == falcon.HTTP_OK

def test_get_stocks_item(client):
    doc = {
            'id' : 1,
            'base': 'AC - RIO BRANCO',
            'value': 415
    }

    response = client.simulate_get('/stocks/1')
    result_doc = response.json

    assert result_doc == doc
    assert response.status == falcon.HTTP_OK

def test_post_with_error_in_data_stock_item(client):
    doc = {
            'id' : 1,
            'base': 'AC - RIO BRANCO',
            'value': 415
    }

    response_doc = {
        "title": "CDD Já existente",
        "description": "Não foi possível criar o registro pois CDD já existe."
    }

    response = client.simulate_post('/stocks',json=doc)
    result_doc = response.json

    assert result_doc == response_doc
    assert response.status == falcon.HTTP_400

def test_update_of_stock_item(client):
    doc = {
            'id' : 1,
            'base': 'AC - RIO BRANCO',
            'value': 415
    }

    response = client.simulate_put('/stocks/1',json=doc)
    result_doc = response.json

    assert result_doc == doc
    assert response.status == falcon.HTTP_OK

def test_error_when_updating_stock_item(client):
    doc = {
            'id' : 1,
            'base': 'AC - RIO BRANCO',
            'value': 'XXXX'
    }

    response_doc = {
        "title": "Atualização Não Realizada",
        "description": "Validar valor informado."
    }

    response = client.simulate_put('/stocks/1',json=doc)
    result_doc = response.json

    assert result_doc == response_doc
    assert response.status == falcon.HTTP_400
