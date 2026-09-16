from unittest.mock import patch
import pytest
import main as app
from src.utils.comida import Comida


@patch("main.crud.crear_comida")
def test_add_meal_success(mock_crear_comida, monkeypatch, capsys):
    """Successful flow: simulate user input and verify the CRUD call."""
    # Configure the mocked return value from crud.crear_comida.
    mock_crear_comida.return_value = {
        "id": 1,
        "nombre": "Pizza Pepperoni",
        "precio": 12.5
    }

    # Console inputs: ID, name, and price.
    respuestas = iter(["1", "Pizza Pepperoni", "12.5"])
    monkeypatch.setattr("builtins.input", lambda _: next(respuestas))

    result = app.agregar_comida()

    # 1. Validate the function return value.
    assert result.id == 1
    assert result.nombre == "Pizza Pepperoni"
    assert result.precio == 12.5

    # 2. Verify that crud.crear_comida was called once with a Comida object.
    mock_crear_comida.assert_called_once()
    args, _ = mock_crear_comida.call_args
    assert isinstance(args[0], Comida)
    assert args[0].id == 1
    assert args[0].nombre == "Pizza Pepperoni"

    # 3. Validate console output.
    captured = capsys.readouterr()
    assert "Comida agregada exitosamente" in captured.out


@patch("main.crud.crear_comida")
def test_add_meal_retries_after_validation_error(mock_crear_comida, monkeypatch, capsys):
    """Verify that CRUD runs only after a valid retry."""
    mock_crear_comida.return_value = {
        "id": 1,
        "nombre": "Pizza",
        "precio": 10.0
    }

    respuestas = iter([
        "-1", "Pizza", "10.0",   # Attempt 1: ID -1 raises ValidationError.
        "1", "Pizza", "10.0"     # Attempt 2: valid data.
    ])
    monkeypatch.setattr("builtins.input", lambda _: next(respuestas))

    result = app.agregar_comida()

    assert result.id == 1

    # Verify that CRUD was called only once after the successful retry.
    mock_crear_comida.assert_called_once()

    captured = capsys.readouterr()
    assert "Datos inválidos. Por favor, intente de nuevo." in captured.out
    assert "Comida agregada exitosamente" in captured.out

@patch("main.crud.obtener_todas")
def test_view_meals(mock_obtener_todas, capsys):
    mock_obtener_todas.return_value = [
        {"id": 1, "nombre": "Pizza", "precio": 10.0},
        {"id": 2, "nombre": "Tacos", "precio": 5.0}
    ]

    app.ver_comidas()

    captured = capsys.readouterr()
    assert "ID: 1, Nombre: Pizza, Precio: 10.0" in captured.out
    assert "ID: 2, Nombre: Tacos, Precio: 5.0" in captured.out
    mock_obtener_todas.assert_called_once()


@patch("main.crud.eliminar_comida")
def test_delete_meal_success(mock_eliminar_comida, monkeypatch, capsys):
    mock_eliminar_comida.return_value = True
    monkeypatch.setattr("builtins.input", lambda _: "1")

    result = app.eliminar_comida()

    assert result == 1
    mock_eliminar_comida.assert_called_once_with(1)
    captured = capsys.readouterr()
    assert "Comida eliminada exitosamente: 1" in captured.out