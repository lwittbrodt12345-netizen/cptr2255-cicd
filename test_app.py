"""Tests for app module - used in CI/CD pipeline."""
import pytest
from app import add, subtract, multiply, divide, is_even, factorial


class TestMathOperations:
    """Test basic math operations."""
    
    def test_add(self):
        assert add(2, 3) == 5
        assert add(-1, 1) == 0
    
    def test_subtract(self):
        assert subtract(5, 3) == 2
        assert subtract(3, 5) == -2
    
    def test_multiply(self):
        assert multiply(3, 4) == 12
        assert multiply(-2, 3) == -6
    
    def test_divide(self):
        assert divide(10, 2) == 5
        assert divide(7, 2) == 3.5
    
    def test_divide_by_zero(self):
        with pytest.raises(ValueError):
            divide(5, 0)


class TestUtilityFunctions:
    """Test utility functions."""
    
    def test_is_even(self):
        assert is_even(2) is True
        assert is_even(3) is False
        assert is_even(0) is True
    
    def test_factorial(self):
        assert factorial(0) == 1
        assert factorial(1) == 1
        assert factorial(5) == 120
    
    def test_factorial_negative(self):
        with pytest.raises(ValueError):
            factorial(-1)
