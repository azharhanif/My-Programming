# Lecture 3: Built-in Functions

### **Table of Contents**

1. [Python Built-In Functions, Packages, and Modules](#python-built-in-functions-packages-and-modules)
2. [Keep It Simple, Stupid (KISS)](#keep-it-simple-stupid-kiss)
3. [Using Trigonometric, Logarithmic, and Exponential Functions](#using-trigonometric-logarithmic-and-exponential-functions)
4. [Comments in Python](#comments-in-python)
5. [Identifying and Fixing Common Errors Using Debugging Techniques](#identifying-and-fixing-common-errors-using-debugging-techniques)


### 1. **Python Built-In Functions, Packages, and Modules**

In Python, **built-in functions**, **packages**, and **modules** are essential tools that make development easier and more efficient. They provide predefined functionality that helps solve common problems.

- **Built-In Functions**: These are functions that Python provides by default, which can be used without any extra setup. Some common built-in functions include:
  - `print()`: Displays output to the user.
  - `len()`: Returns the length of an object (e.g., a string or list).
  - `int()`, `float()`, `str()`: Convert values between different data types.

Example:
```python
name = "Alice"
length = len(name)  # Using the built-in len() function to find the length of the string
print(length)  # Output: 5
```

- **Packages**: A package is a collection of related modules bundled together. You can install packages using Python’s package manager, `pip`, which provides additional functionality beyond the built-in features.

Example:
```python
# To use the math package, you must first import it
import math

# Now you can access all the functions in the math module, like sqrt()
result = math.sqrt(16)  # Result is 4.0
```

- **Modules**: A module is a single file that contains functions, classes, and variables that you can import into your program to reuse. For example, the `math` module provides functions for mathematical operations.

### 2. **Keep It Simple, Stupid (KISS)**

The **KISS principle** emphasizes keeping solutions simple and straightforward. In programming, this means writing code that is easy to read, understand, and maintain. Avoid overcomplicating problems or adding unnecessary complexity.

Key takeaways:
- **Write simple code**: Focus on clarity and simplicity instead of trying to make the code overly efficient or complex.
- **Use existing tools**: Leverage built-in functions, packages, and modules rather than reinventing the wheel.

Example (KISS principle):
Instead of writing a complex loop to find the maximum value in a list, use Python's built-in `max()` function:
```python
numbers = [1, 2, 3, 4, 5]
max_value = max(numbers)  # Simple and efficient way to get the max value
print(max_value)  # Output: 5
```

### 3. **Using Trigonometric, Logarithmic, and Exponential Functions from the Python Math Library**

Python’s **math library** provides a wide range of mathematical functions, including trigonometric, logarithmic, and exponential operations. These functions help solve various problems in science and engineering.

Common functions in the `math` module:
- **Trigonometric Functions**: `sin()`, `cos()`, `tan()`, `asin()`, `acos()`, `atan()`
- **Logarithmic Functions**: `log()`, `log10()`, `log2()`
- **Exponential Function**: `exp()`

Example of using the **math** module:
```python
import math

# Trigonometric example: sine of 30 degrees
angle_radians = math.radians(30)  # Convert degrees to radians
sine_value = math.sin(angle_radians)
print("Sine of 30 degrees:", sine_value)  # Output: 0.49999999999999994

# Logarithmic example: natural log of 10
log_value = math.log(10)
print("Log of 10:", log_value)  # Output: 2.302585092994046

# Exponential example: e raised to the power of 2
exp_value = math.exp(2)
print("Exponential of 2:", exp_value)  # Output: 7.3890560989306495
```

These functions are useful for scientific applications that involve angles, logarithms, or growth models (such as in physics, biology, and economics).

### 4. **Comments in Python**

**Comments** in Python are lines of text that are ignored by the interpreter. They are used to explain and document code, making it easier to understand for other developers (or your future self).

- **Single-line comments** are created by adding a `#` before the comment.
- **Multi-line comments** can be created using triple quotes (`'''` or `"""`), though these are generally used for docstrings (documentation strings).

Example of single-line and multi-line comments:
```python
# This is a single-line comment

# Function to calculate speed
def calculate_speed(distance, time):
    '''This function calculates speed based on distance and time.'''
    speed = distance / time  # Speed calculation
    return speed

# Call the function
print(calculate_speed(100, 20))  # Output: 5.0
```

Comments are essential for maintaining and understanding code, especially when the program becomes more complex.

### 5. **Identifying and Fixing Common Errors Using Debugging Techniques**

**Debugging** is an essential skill in programming that involves identifying and fixing errors in code. Common errors in Python include **syntax errors**, **runtime errors**, and **logical errors**.

#### Common Debugging Techniques:
1. **Read error messages carefully**: Python provides useful error messages that tell you where the problem is in your code. Always read these messages to understand what went wrong.
2. **Use print statements**: Print the values of variables or the result of expressions to help understand what the program is doing at different points.
3. **Check for common mistakes**:
   - Missing or extra parentheses
   - Typographical errors in variable or function names
   - Incorrect indentation (Python relies on indentation to define code blocks)

Example of debugging with print statements:
```python
# Debugging an example of calculating speed
distance = float(input("Enter distance: "))
time = float(input("Enter time: "))

# Debugging: Check the inputs before calculating
print("Distance entered:", distance)
print("Time entered:", time)

# Perform calculation
speed = distance / time

# Output the result
print(f"Speed is {speed} meters per second.")
```

In this example, **print statements** are used to check if the inputs are correct before performing the calculation. This helps identify if the problem lies with the inputs or the calculation itself.

---


## New-Semester Learning Cycle

For each major example, use this sequence:

1. **Read the problem**
2. **Predict** what the code should do
3. **Trace** the important variables
4. **Code** the smallest working version
5. **Run and inspect**
6. **Debug** one problem at a time
7. **Modify** the solution
8. **Explain the design choice**

The goal is not to make the course easier. The goal is to make the reasoning visible so that a student who is still developing programming fluency can follow the path from a scientific problem to a correct Python solution.


---

# Lecture 3: Built-in Functions, Modules, and Debugging

## 0. Why this lecture matters

A common beginner mistake is to think programming means writing every operation yourself. Python already provides many reliable operations. Good programmers learn to recognize when a problem has already been solved by a built-in function or standard library module.

The challenge is **not merely knowing function names**. It is deciding:

> "What tool is appropriate, what type does it expect, and what does it return?"

## 1. Predict Before Running

```python
x = "Vanier"
print(len(x))
print(max([4, 2, 9, 1]))
print(round(3.14159, 2))
```

Predict each output first.

Then explain:

- What is the input to each function?
- What is the return value?
- Does the function modify the original object?

## 2. Built-in Function vs Module

Built-in:

```python
length = len("Programming")
```

No import is required.

Module:

```python
import math

answer = math.sqrt(81)
```

The `math` module groups related mathematical operations.

Think:

```text
Python built-in → available directly
module function → import module, then use module.function()
```

## 3. Scientific Example: Unit Conversion

Suppose an angle is supplied in degrees:

```python
import math

degrees = 30
radians = math.radians(degrees)
result = math.sin(radians)

print(result)
```

### Why is `math.radians()` important?

Most trigonometric functions in `math` expect radians.

A program can be syntactically correct and scientifically wrong.

This distinction is important:

> **A program that runs without an error is not necessarily a correct scientific program.**

## 4. KISS: Use the Tool That Matches the Problem

Instead of:

```python
numbers = [3, 8, 2, 10]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number
```

Python already provides:

```python
largest = max(numbers)
```

The loop is not always wrong. It is useful when the exercise is specifically about algorithmic reasoning. But in production code, `max()` is clearer when that is all we need.

## 5. Comments: Explain Why

Weak comment:

```python
x = x + 1  # add 1 to x
```

Better:

```python
# Move to the next experimental measurement.
x = x + 1
```

Comments should explain reasoning, assumptions, units, or non-obvious decisions—not narrate every line.

## 6. Debugging as a Process

When code fails:

```text
1. Read the error.
2. Locate the line.
3. Identify the error category.
4. Inspect the values/types.
5. Predict what should happen.
6. Change one thing.
7. Run again.
```

### Example

```python
distance = input("Distance: ")
time = input("Time: ")

speed = distance / time
```

The problem is not the formula. The problem is the types.

```python
distance = float(input("Distance: "))
time = float(input("Time: "))
```

Now ask the next question:

> What happens when `time == 0`?

This leads naturally to defensive programming.

## 7. Debugging Challenge

Find the problem:

```python
import math

angle = 90
value = math.sin(angle)

print(value)
```

The program runs. Is it correct?

Fix it and explain why.

## 8. Active-Learning Questions

1. Predict `math.sin(math.radians(90))`.
2. Why can `math.sin(90)` be surprising to a beginner?
3. When is writing a loop preferable to using `max()`?
4. Which is more useful in a comment: "calculate x" or "convert degrees to radians because math.sin expects radians"? Why?
5. A program produces a plausible number but the units are wrong. Is that a bug? Explain.

## 9. Mini Challenge

Write a program that asks for:

- angle in degrees;
- distance in metres;

and calculates:

```text
horizontal_component = distance * cos(angle)
vertical_component   = distance * sin(angle)
```

Requirements:

- use `math`;
- convert degrees to radians;
- print both results;
- test at least `0`, `30`, `90`, and `180` degrees;
- explain one result that you can predict without running the program.
