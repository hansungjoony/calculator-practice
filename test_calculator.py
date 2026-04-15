import pytest
from calculator import add, subtract, multiply, divide


class TestAdd:
    def test_add_positive(self):
        assert add(2, 3) == 5

    def test_add_negative(self):
        assert add(-1, -2) == -3

    def test_add_zero(self):
        assert add(5, 0) == 5


class TestSubtract:
    def test_subtract_basic(self):
        assert subtract(10, 4) == 6

    def test_subtract_negative_result(self):
        assert subtract(3, 7) == -4


class TestMultiply:
    def test_multiply_basic(self):
        assert multiply(3, 4) == 12

    def test_multiply_by_zero(self):
        assert multiply(5, 0) == 0

    def test_multiply_negatives(self):
        assert multiply(-2, 3) == -6


class TestDivide:
    def test_divide_basic(self):
        assert divide(10, 2) == 5.0

    def test_divide_float_result(self):
        assert divide(7, 2) == 3.5

    def test_divide_by_zero_raises(self):
        with pytest.raises(ValueError):
            divide(5, 0)