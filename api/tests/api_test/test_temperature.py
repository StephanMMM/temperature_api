import pytest

from fastapi import status
from starlette.testclient import TestClient

from ...src import main

test_client = TestClient(main.api)

def test_temperature_conversion_valid_1(valid_temperature_data_1):
    response = test_client.post("/temperature/convert", json=valid_temperature_data_1)
    response_data = response.json()
    assert response.status_code == status.HTTP_200_OK
    assert response_data["degrees"] == 95
    assert response_data["unit"] == valid_temperature_data_1["new_unit"]

def test_temperature_conversion_valid_2(valid_temperature_data_2):
    response = test_client.post("/temperature/convert", json=valid_temperature_data_2)
    response_data = response.json()
    assert response.status_code == status.HTTP_200_OK
    assert response_data["degrees"] == 5
    assert response_data["unit"] == valid_temperature_data_2["new_unit"]

def test_temperature_conversion_invalid_unit(invalid_temperature_data_1):
    response = test_client.post("/temperature/convert", json=invalid_temperature_data_1)
    assert response.status_code == status.HTTP_404_NOT_FOUND

@pytest.fixture
def valid_temperature_data_1():
    data = {
        "degrees": 35,
        "unit": "celsius",
        "new_unit": "fahrenheit"
    }
    return data

@pytest.fixture
def valid_temperature_data_2():
    data = {
        "degrees": 41,
        "unit": "fahrenheit",
        "new_unit": "celsius"
    }
    return data

@pytest.fixture
def invalid_temperature_data_1():
    data = {
        "degrees": 41,
        "unit": "celsius",
        "new_unit": "kelvin"
    }
    return data