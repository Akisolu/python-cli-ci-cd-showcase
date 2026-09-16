import pytest
from pydantic import ValidationError
from src.utils.id_comida import IdInput

@pytest.mark.parametrize("input_value, expected", [
    ("1", 1),
    ("100", 100),
    ("9999", 9999),
])
def test_id_input_valid(input_value, expected):
    validator = IdInput(id_comida=input_value)
    assert validator.id_comida == expected

@pytest.mark.parametrize("input_value", [
    "abc",    # Non-numeric text
    "0",      # Out of range (must be > 0)
    "-1",     # Negative integer
    "1.5",    # Float
    "",       # Empty string
])
def test_id_input_invalid(input_value):
    with pytest.raises(ValidationError):
        IdInput(id_comida=input_value)