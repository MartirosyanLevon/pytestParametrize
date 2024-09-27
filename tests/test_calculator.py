from contextlib import nullcontext as does_not_raise

import pytest

from src.calculator import Calculator


class TestCalculator:
    @pytest.mark.parametrize(
        "x, y, res, expectation",
        [
            # Normal case: positive integers
            (1, 2, 0.5, does_not_raise()),
            # Dividing by a negative number
            (5, -1, -5, does_not_raise()),
            # Invalid input: string
            (5, "-1", None, pytest.raises(TypeError)),\
            # Dividing by zero
            (5, 0, None, pytest.raises(ZeroDivisionError)),  
            # Dividing two negative numbers
            (-4, -2, 2, does_not_raise()),
            # Dividing by a floating-point number
            (5, 0.5, 10.0, does_not_raise()),
            # Dividing float by an integer
            (5.5, 2, 2.75, does_not_raise()),
            # Dividing large numbers
            (1000000000, 2000000, 500.0, does_not_raise()),
            # Dividing zero by a number
            (0, 5, 0, does_not_raise()),
        ]
    )
    def test_divide(self, x, y, res, expectation):
        with expectation:
            assert Calculator().divide(x, y) == res

    @pytest.mark.parametrize(
        "x, y, res, expectation",
        [
            # Normal case: two integers
            (1, 2, 3, does_not_raise()),
            # Positive and negative integers
            (5, -1, 4, does_not_raise()),
            # Integer and string (invalid)
            (5, "-1", None, pytest.raises(TypeError)),
            # Edge case: two zeros
            (0, 0, 0, does_not_raise()),
            (1000000000, 2000000000, 3000000000,
             does_not_raise()),  # Large numbers
            # Floating-point numbers
            (1.5, 2.5, 4.0, does_not_raise()),
            # Invalid input: None and integer
            (None, 5, None, pytest.raises(TypeError)),
            # Two negative numbers
            (-3, -7, -10, does_not_raise()),
            # Positive and negative floats
            (1.5, -2.5, -1.0, does_not_raise()),
            # Invalid input: Two strings
            ("5", "3", None, pytest.raises(TypeError)),
        ]
    )
    def test_add(self, x, y, res, expectation):
        with expectation:
            assert Calculator().add(x, y) == res

    @pytest.mark.parametrize(
        "x, y, res, expectation",
        [
            # Basic multiplication
            (2, 3, 6, does_not_raise()),
            # Multiplying by zero
            (5, 0, 0, does_not_raise()),
            # Multiplying by one
            (7, 1, 7, does_not_raise()),
            # Multiplying by a negative number
            (-5, 3, -15, does_not_raise()),
            # Multiplying two negative numbers
            (-4, -2, 8, does_not_raise()),
            # Multiplying float by integer
            (1.5, 2, 3.0, does_not_raise()),
            # Large number multiplication
            (1000000, 1000, 1000000000, does_not_raise()),
            # Multiplying floating-point numbers
            (2.5, -1.2, -3.0, does_not_raise()),
            # Invalid input: string
            (5, "2", None, pytest.raises(TypeError)),
        ]
    )
    def test_multiply(self, x, y, res, expectation):
        with expectation:
            assert Calculator().multiply(x, y) == res

    @pytest.mark.parametrize(
        "x, y, res, expectation",
        [
            # Basic subtraction
            (5, 3, 2, does_not_raise()),
            # Subtracting zero
            (7, 0, 7, does_not_raise()),
            # Subtracting a number from itself
            (10, 10, 0, does_not_raise()),
            # Subtracting a larger number from a smaller one
            (3, 5, -2, does_not_raise()),
            # Subtracting two negative numbers
            (-5, -3, -2, does_not_raise()),
            # Subtracting floating-point numbers
            (5.5, 2.5, 3.0, does_not_raise()),
            # Subtracting large numbers
            (1000000, 500000, 500000, does_not_raise()),
            # Invalid input: string
            (5, "2", None, pytest.raises(TypeError)),
        ]
    )
    def test_subtract(self, x, y, res, expectation):
        with expectation:
            assert Calculator().subtract(x, y) == res
