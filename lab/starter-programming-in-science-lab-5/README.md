# Programming in Science - Lab 5

This template repository is the starter project for Programming in Science Lab 5. Written in Python, and tested with Pytest.

### Question(s) 

1. Write a function `hollow_square(n)` that returns a string representing a hollow square pattern of stars (`*`) with side length `n`.

#### Example (n = 5):
```
*****
*   *
*   *
*   *
*****
```
✅ **Hints:** Use a `while` loop and construct each line, appending them to a result string.

2. Write a function `number_pattern(n)` that returns a string representing a number pattern of height `n` **without using a `for` loop inside the print statement**.

#### Example (n = 4):
```
1
12
123
1234
```
✅ **Hints:** Use nested `while` loops to build the pattern.

3. Write a function `sum_of_natural_numbers(n)` that **returns the sum** of the first `n` natural numbers using a `while` loop.

#### Example:
For `n = 5`:
```
Sum = 1 + 2 + 3 + 4 + 5 = 15
```
✅ **Hints:** Use a counter variable and accumulate the total.

4. Write a function `centered_star_pyramid(n)` that returns a string representing a centered pyramid of stars (`*`) with height `n`.

#### Example (n = 4):
```
   *
  ***
 *****
*******
```
✅ **Hints:** Use spaces before stars to center the pyramid.

### Run Command

`pytest`