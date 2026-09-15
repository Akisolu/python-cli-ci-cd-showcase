import json
from unittest.mock import patch, mock_open
import pytest

from src import crud
from src.utils.comida import Comida

COMIDAS_MOCK = [
    {"id": 1, "nombre": "Pizza", "precio": 10.99},
    {"id": 2, "nombre": "Hamburguesa", "precio": 8.50}
]

# ==========================================
# 1. READ TESTS
# ==========================================

@patch("pathlib.Path.exists", return_value=True)
@patch("builtins.open", new_callable=mock_open, read_data=json.dumps(COMIDAS_MOCK))
def test_get_all_meals_success(mock_file, mock_exists):
    result = crud.obtener_todas()
    assert len(result) == 2
    assert result[0]["nombre"] == "Pizza"


@patch("pathlib.Path.exists", return_value=True)
@patch("builtins.open", new_callable=mock_open, read_data=json.dumps(COMIDAS_MOCK))
def test_get_meal_by_existing_id(mock_file, mock_exists):
    result = crud.obtener_por_id(1)
    assert result is not None
    assert result["id"] == 1
    assert result["nombre"] == "Pizza"


@patch("pathlib.Path.exists", return_value=True)
@patch("builtins.open", new_callable=mock_open, read_data=json.dumps(COMIDAS_MOCK))
def test_get_meal_by_missing_id(mock_file, mock_exists):
    result = crud.obtener_por_id(99)
    assert result is None


@patch("pathlib.Path.exists", return_value=False)
def test_load_data_when_file_does_not_exist(mock_exists):
    result = crud._cargar_datos()
    assert result == []


@patch("pathlib.Path.exists", return_value=True)
@patch("builtins.open", new_callable=mock_open, read_data="JSON_INVALIDO{{{")
def test_load_data_with_corrupted_json(mock_file, mock_exists):
    result = crud._cargar_datos()
    assert result == []


# ==========================================
# 2. CREATION TESTS
# ==========================================

@patch("src.crud._guardar_datos")
@patch("src.crud._cargar_datos", return_value=[])
def test_create_meal_without_id(mock_cargar, mock_guardar):
    new_meal = Comida(nombre="Tacos", precio=5.0)
    result = crud.crear_comida(new_meal)
    
    assert result["id"] == 1
    assert result["nombre"] == "Tacos"
    mock_guardar.assert_called_once()


@patch("src.crud._guardar_datos")
@patch("src.crud._cargar_datos", return_value=[{"id": 1, "nombre": "Pizza", "precio": 10.99}])
def test_create_meal_increments_id(mock_cargar, mock_guardar):
    new_meal = Comida(nombre="Sushi", precio=15.0)
    result = crud.crear_comida(new_meal)
    
    assert result["id"] == 2
    mock_guardar.assert_called_once()


# ==========================================
# 3. DELETION TESTS
# ==========================================

@patch("src.crud._guardar_datos")
@patch("src.crud._cargar_datos", return_value=[{"id": 1, "nombre": "Pizza", "precio": 10.99}])
def test_delete_meal_success(mock_cargar, mock_guardar):
    success = crud.eliminar_comida(1)
    assert success is True
    mock_guardar.assert_called_once_with([])


@patch("src.crud._guardar_datos")
@patch("src.crud._cargar_datos", return_value=[{"id": 1, "nombre": "Pizza", "precio": 10.99}])
def test_delete_missing_meal(mock_cargar, mock_guardar):
    success = crud.eliminar_comida(99)
    assert success is False
    mock_guardar.assert_not_called()