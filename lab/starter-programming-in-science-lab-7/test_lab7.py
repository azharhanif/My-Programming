import unittest
from Lab7 import rotate_the_array, jump_game

# Test case for rotate_the_array() function
def test_rotate_the_array():
    assert rotate_the_array(11, 0) == [24, 27, 18, 21, 12, 15, 6, 9, 0, 3, 30]
    assert rotate_the_array(5, 1) == [7, 10, 1, 4, 13]

# Test case for jump_game() function
def test_jump_game():
    assert jump_game([2, 3, 1, 1, 4]) == 2
    assert jump_game([2, 3, 0, 1, 4]) == 2

if __name__ == '__main__':
    unittest.main()
