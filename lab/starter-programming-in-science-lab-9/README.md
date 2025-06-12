# Programming in Science - Lab 9

This template repository is the starter project for **Programming in Science Lab 9**. Written in Python and tested with Pytest.

### Question(s)

1. **(30%)** Read values from a file:
   
   - Write a function `read_values_from_file(filename)` that reads numerical values from a text file and stores them in a NumPy array.
   
   #### Example:
   ```python
   read_values_from_file("values.txt")  # Returns a NumPy array of values
   ```
   ✅ **Hints:** Ensure the file contains one numerical value per line.

2. **(30%)** Read Oscillatory Wave Data:
   
   - Write a function `read_oscillatory_wave_data(filename)` that reads a file containing wave data with length and amplitude values. Compute the mean and maximum amplitude.
   
   #### Example:
   ```python
   read_oscillatory_wave_data("wave_data.csv")
   ```
   ✅ **Hints:** Use NumPy to read the CSV and compute statistics.

3. **(40%)** Read Standing Wave Data:
   
   - Write a function `read_standing_wave_data(filename)` that reads a file containing standing wave data with length and tension values. Compute the wave speed using:
   
   Wave speed is calculated using the formula:

  **v = sqrt(T / μ)**

  where **T** is tension and **μ** (mass per unit length) is assumed to be 1.
   
   where \( \mu \) (mass per unit length) is assumed to be 1.
   
   #### Example:
   ```python
   read_standing_wave_data("standing_wave.csv")
   ```
   ✅ **Hints:** Use NumPy to read the CSV and compute the wave speed.

### Run Command

To run the tests, use the following command:

```
pytest
```

