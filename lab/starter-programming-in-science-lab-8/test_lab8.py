import unittest
from Lab8 import is_magic_square, generate_magic_square

# Test case for is_magic_square() function
def test_is_magic_square():
    assert is_magic_square([[4, 9, 2], [3, 5, 7], [8, 1, 6]]) == True
    assert is_magic_square([[4, 9, 2], [8, 1, 6], [3, 5, 7]]) == False

# Test case for generate_magic_square() function
def test_generate_magic_square():
    assert generate_magic_square(3) == [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
    assert generate_magic_square(5) == [
        [11, 18, 25, 2, 9],
        [10, 12, 19, 21, 3],
        [4, 6, 13, 20, 22],
        [23, 5, 7, 14, 16],
        [17, 24, 1, 8, 15]
    ]

if __name__ == '__main__':
    unittest.main()