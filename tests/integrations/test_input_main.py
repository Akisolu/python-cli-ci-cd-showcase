import pytest
from pydantic import ValidationError
import main as m

# ==========================================
# 1. VALID CASES (Range 1 to 4)
# ==========================================

@pytest.mark.parametrize("input_value, expected", [
    ("1", 1),  # Lower bound
    ("2", 2),  # Middle value
    ("3", 3),  # Middle value
    ("4", 4),  # Upper bound
])
def test_validate_menu_option_valid(input_value, expected):
    result = m.validar_opcion_menu(input_value)
    assert result == expected


# ==========================================
# 2. INVALID CASES (Raises ValidationError)
# ==========================================

@pytest.mark.parametrize("input_value", [
    "abc",    # Non-numeric string
    "-1",     # Out of range (below 1)
    "0",      # Out of range (below 1)
    "5",      # Out of range (above 4)
    "99",     # Out of range
    "1.5",    # Float represented as a string
    "True",   # Boolean represented as console text
    "",       # Empty string
])
def test_validate_menu_option_invalid(input_value):
    with pytest.raises(ValidationError):
        m.validar_opcion_menu(input_value)