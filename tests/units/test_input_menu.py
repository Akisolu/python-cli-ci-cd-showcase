import pytest
from pydantic import ValidationError
from src.utils.input_menu import OpcionInput


# ==========================================
# 1. VALID CASES (Range 1 to 4)
# ==========================================

@pytest.mark.parametrize("input_value, expected", [
    ("1", 1),
    ("2", 2),
    ("3", 3),
    ("4", 4),
])
def test_menu_option_input_valid(input_value, expected):
    # Directly instantiate the model from src/utils/input_menu.py.
    validator = OpcionInput(opcion=input_value)
    assert validator.opcion == expected


# ==========================================
# 2. INVALID CASES (Raises ValidationError)
# ==========================================

@pytest.mark.parametrize("input_value", [
    "abc",    # Non-numeric text
    "-1",     # Below the lower bound
    "0",      # Below the lower bound
    "5",      # Above the upper bound
    "99",     # Out of range
    "1.5",    # Float
    "True",   # Boolean represented as a string
    "",       # Empty string
])
def test_menu_option_input_invalid(input_value):
    with pytest.raises(ValidationError):
        OpcionInput(opcion=input_value)