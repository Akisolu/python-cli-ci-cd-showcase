import pytest
from pydantic import ValidationError
import src.utils.comida as c

# ==========================================
# 1. HAPPY PATHS AND EDGE CASES (Parametrized)
# ==========================================

@pytest.mark.parametrize("id_value, name, price", [
    (5, "Pizza", 10.99),                 # Standard happy path
    (None, "Arroz", 12.00),               # Optional ID/None
    (1, "a", 0.1),                        # Minimum/short values
    (12345678, "abcdefghijkl", 12345678.90) # Large values
])
def test_meal_creation_success(id_value, name, price):
    comida = c.Comida(id=id_value, nombre=name, precio=price)
    
    assert comida.id == id_value
    assert comida.nombre == name
    assert comida.precio == price


# ==========================================
# 2. ERROR CASES (ValidationErrors)
# ==========================================

@pytest.mark.parametrize("invalid_id", [
    "abc",   # Non-numeric string
    -1,      # Negative integer
    -99,     # Large negative integer
    True,    # Boolean
    1.5,     # Float
])
def test_invalid_meal_id(invalid_id):
    with pytest.raises(ValidationError):
        c.Comida(id=invalid_id, nombre="Pizza", precio=10.99)


@pytest.mark.parametrize("invalid_name", [
    123,     # Number
    "",      # Empty string
    None,    # Missing name
    True,    # Boolean
])
def test_invalid_meal_name(invalid_name):
    with pytest.raises(ValidationError):
        c.Comida(id=1, nombre=invalid_name, precio=10.99)


@pytest.mark.parametrize("invalid_price", [
    "abc",    # String not convertible to float
    -10.99,   # Negative price
    None,     # Missing price
    True,     # Boolean
])
def test_invalid_meal_price(invalid_price):
    with pytest.raises(ValidationError):
        c.Comida(id=1, nombre="Pizza", precio=invalid_price)