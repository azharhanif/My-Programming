import unittest
from Lab6 import factorial, fibonacci, is_prime

# Test case for factorial() function
def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(7) == 5040
    assert factorial(10) == 3628800

# Test case for fibonacci() function
def test_fibonacci():
    assert fibonacci(1) == 0
    assert fibonacci(2) == 1
    assert fibonacci(5) == 3
    assert fibonacci(7) == 8
    assert fibonacci(10) == 34

# Test case for is_prime() function
def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(11) == True
    assert is_prime(15) == False
    assert is_prime(17) == True

if __name__ == '__main__':
    unittest.main()
