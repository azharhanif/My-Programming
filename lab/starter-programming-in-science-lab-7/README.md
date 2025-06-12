# Programming in Science - Lab 7

This template repository is the starter project for **Programming in Science Lab 7**. Written in Python, and tested with Pytest.

### Question(s)

1. **(50%)** Rotate the Array:
   
   - Write a function `rotate_the_array(array_size, starting_integer)` that **creates an array** of a specified size, fills it with numbers starting from `starting_integer` and decreasing by 3, then rotates elements at even indices 2 positions to the left.

   ![](Q1.png)
   
   #### Example:
   ```python
   rotate_the_array(11, 0)  # Returns [24, 27, 18, 21, 12, 15, 6, 9, 0, 3, 30]
   rotate_the_array(5, 1)   # Returns [7, 10, 1, 4, 13]
   ```
   ✅ **Hints:** Generate the sequence, then shift elements at even indices.

2. **(50%)** Jump Game:
   
   - Write a function `jump_game(nums)` that returns the **minimum number of jumps** needed to reach the last index in the array.
   
   #### Example:
   ```python
   jump_game([2, 3, 1, 1, 4])  # Returns 2
   jump_game([2, 3, 0, 1, 4])  # Returns 2
   ```
   ✅ **Hints:** Use **greedy algorithm** to find the optimal jumps.

### Run Command

To run the tests, use the following command:

```
pytest
```