import pytest
import math
from geometry_calculator import (
    area_circle, area_rectangle,
    area_triangle, area_trapezoid
)

class TestCircle:
    def test_basic(self):
        result = area_circle(5)
        assert abs(result - 78.539) < 0.01

    def test_zero(self):
        assert area_circle(0) == 0.0

    def test_negative_raises(self):
        with pytest.raises(ValueError):
            area_circle(-1)

class TestRectangle:
    def test_basic(self):
        assert area_rectangle(4, 6) == 24.0

    def test_square(self):
        assert area_rectangle(5, 5) == 25.0

    def test_zero_side(self):
        assert area_rectangle(0, 10) == 0.0

class TestTriangle:
    def test_basic(self):
        assert area_triangle(3, 8) == 12.0

    def test_half_formula(self):
        assert area_triangle(10, 4) == 20.0

class TestTrapezoid:
    def test_basic(self):
        assert area_trapezoid(3, 7, 4) == 20.0

    def test_same_sides_is_rectangle(self):
        assert area_trapezoid(5, 5, 6) == 30.0
