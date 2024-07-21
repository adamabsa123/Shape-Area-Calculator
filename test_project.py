import math
import pytest
from project import calculate_rectangle, calculate_circle, calculate_triangle

def test_rectangle():
    assert calculate_rectangle(5, 10) == 50

def test_circle():
    answer = math.pi * 3 * 3
    final_answer = calculate_circle(3)
    assert math.isclose(final_answer, answer, rel_tol=1e-2)

def test_triangle():
    assert calculate_triangle(4, 6) == 12
