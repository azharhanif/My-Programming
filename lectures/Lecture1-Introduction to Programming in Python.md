# Lecture 1: Introduction to Programming in Python — New Semester

## Course learning philosophy

Programming is not primarily about remembering syntax. It is about turning a problem into precise instructions that a computer can execute.

Throughout this course we will use:

> **Understand → Predict → Code → Run → Test → Debug → Explain → Modify**

If you can make code run but cannot explain why it works, you do not yet fully understand the solution.

## 1. Introduction to Programming

A programming language such as Python allows humans to communicate instructions to a computer. In scientific programming, those instructions often transform measurements, formulas, and experimental data into useful results.

A useful model is:

```text
Problem → Inputs/Outputs → Algorithm → Python → Tests → Result
```

### Worked example: Celsius to Fahrenheit

Formula:

```text
F = C × 9/5 + 32
```

Analyze first:

- Input: Celsius temperature
- Output: Fahrenheit temperature
- Operation: multiply by 9/5, then add 32

```python
celsius = 20
fahrenheit = celsius * 9 / 5 + 32
print(fahrenheit)
```

### Predict before running

```python
celsius = 0
fahrenheit = celsius * 9 / 5 + 32
print(fahrenheit)
```

Expected output: `32.0`.

The important skill is being able to trace the calculation, not memorizing the answer.

## 2. Statements and Expressions

A **statement** performs an action:

```python
x = 10
print(x)
```

An **expression** produces a value:

```python
x + 5
```

In:

```python
x = x + 5
```

`x + 5` is evaluated first, then its value is assigned to `x`.

### Trace

```python
x = 4
x = x + 3
x = x * 2
print(x)
```

Trace:

```text
4 → 7 → 14
```

Output: `14`.

## 3. Variables and Assignment

A variable is a name associated with a value.

```python
age = 20
name = "Amina"
height = 1.72
```

Python is dynamically typed, so a type declaration is not required.

Prefer descriptive names:

```python
distance_m = 120
elapsed_time_s = 8
```

over:

```python
a = 120
b = 8
```

Use `snake_case` for variables and functions.

### Think

Which is easier to explain six weeks later?

```python
x = d / t
```

or

```python
speed_m_per_s = distance_m / time_s
```

The second communicates meaning and units.

## 4. Data Types

Common Python types:

| Type | Example |
|---|---|
| `int` | `5` |
| `float` | `5.7` |
| `str` | `"hello"` |
| `bool` | `True` |
| `list` | `[1, 2, 3]` |
| `tuple` | `(1, 2, 3)` |

Use `type()` when debugging:

```python
x = 10
print(type(x))
```

### Predict

```python
x = 10
x = x / 4
print(type(x))
```

The result is a `float` because `/` produces floating-point division.

## 5. Input and Output

`input()` returns a string:

```python
name = input("Enter your name: ")
```

Convert numeric input explicitly:

```python
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))
```

Example:

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))

print("Hello,", name)
print("You are", age, "years old.")
print("Your height is", height, "meters.")
```

### Debugging question

If `int(input(...))` fails, ask:

> What exact string did the user enter, and can Python convert it to an integer?

## 6. Arithmetic Operations

```text
+  addition
-  subtraction
*  multiplication
/  division
// floor division
%  remainder
** exponentiation
```

Example:

```python
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
```

Use parentheses when they make the intended mathematics clearer.

```python
result = (2 + 3) * 4
```

## 7. First Scientific Calculation

For an object travelling distance `d` in time `t`:

```text
speed = distance / time
```

Before coding ask:

1. What are the inputs?
2. What are their units?
3. What is the formula?
4. What output and unit are expected?
5. What edge case could break the calculation?

Example:

```python
distance_m = 100
time_s = 20
speed_m_per_s = distance_m / time_s
print("Speed:", speed_m_per_s, "m/s")
```

## 8. Algorithms Before Code

For the speed problem:

```text
1. Obtain distance.
2. Obtain time.
3. Check that time is not zero.
4. Divide distance by time.
5. Report speed in m/s.
```

Then translate the algorithm into Python.

This separation helps distinguish a wrong **algorithm** from a wrong **Python implementation**.

## 9. Early Testing and Debugging

Test small pieces as you write them.

```python
print("distance =", distance_m)
print("time =", time_s)
print("speed =", speed_m_per_s)
```

Test normal and edge cases:

```text
normal: distance=100, time=20
small: distance=1, time=0.5
edge: time=0
```

A program can be syntactically correct but logically wrong. Testing is how we discover that difference.

## 10. Reading Error Messages

Treat a traceback as information.

When an error occurs, identify:

1. exception type;
2. line where it occurred;
3. operation that failed;
4. input/state that caused it.

Do not immediately rewrite the whole program.

## 11. KISS, DRY, Open/Closed

**KISS:** keep solutions clear and appropriately simple.

**DRY:** repeated logic should eventually become reusable code, often a function.

**Open/Closed:** design reusable pieces that can be extended rather than repeatedly rewritten. We will revisit this idea later.

## 12. Active Learning Checkpoints

### Checkpoint 1
Predict:

```python
x = 5
x = x + 2
x = x * 3
print(x)
```

### Checkpoint 2
What type is produced?

```python
result = 7 / 2
```

### Checkpoint 3
What is wrong?

```python
age = input("Age: ")
print(age + 5)
```

### Checkpoint 4
For "Calculate distance travelled by a car moving at 20 m/s for 7 seconds", identify inputs, output, formula, and units.

### Checkpoint 5
What edge case should be tested for `speed = distance / time`?

Explain your reasoning, not just your answer.

## Summary

A strong programmer repeatedly moves between the problem, the algorithm, and the code:

```text
Understand → Predict → Code → Test → Debug → Explain → Modify
```

Your code is the implementation of your reasoning, not a substitute for reasoning.
