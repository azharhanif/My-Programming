import unittest
from Lab5 import hollow_square, number_pattern, sum_of_natural_numbers, centered_star_pyramid

# Test hollow_square function
def test_hollow_square():
    assert hollow_square(5) == "*****\n*   *\n*   *\n*   *\n*****"
    assert hollow_square(2) == "**\n**"
    assert hollow_square(1) == "*"

# Test number_pattern function
def test_number_pattern():
    assert number_pattern(4) == "1\n12\n123\n1234"
    assert number_pattern(1) == "1"
    assert number_pattern(3) == "1\n12\n123"

# Test sum_of_natural_numbers function
def test_sum_of_natural_numbers():
    assert sum_of_natural_numbers(5) == 15  # 1+2+3+4+5 = 15
    assert sum_of_natural_numbers(1) == 1
    assert sum_of_natural_numbers(0) == 0
    assert sum_of_natural_numbers(10) == 55
    assert sum_of_natural_numbers(3) == 6  # 1+2+3 = 6

# Test centered_star_pyramid function
def test_centered_star_pyramid():
    assert centered_star_pyramid(4) == "   *\n  ***\n *****\n*******"
    assert centered_star_pyramid(1) == "*"
    assert centered_star_pyramid(3) == "  *\n ***\n*****"

# Run tests
if __name__ == '__main__':
    test_hollow_square()
    test_number_pattern()
    test_sum_of_natural_numbers()
    test_centered_star_pyramid()
    print("All tests passed!")

