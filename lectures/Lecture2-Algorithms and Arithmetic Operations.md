# Lecture 2: Algorithms and Arithmetic Operations — New Semester

## Teaching goal

Lecture 2 moves from Python syntax to problem-solving. The central question is:

> **How do we turn a scientific problem statement into a reliable program?**

Use:

```text
Problem → Inputs/Outputs → Formula/Assumptions → Algorithm → Trace → Code → Test → Debug
```

## 1. What Is an Algorithm?

An algorithm is a finite, ordered set of steps for solving a problem. It is independent of a particular programming language.

Example: rectangle area

```text
1. Read length.
2. Read width.
3. Calculate length × width.
4. Display area.
```

Python:

```python
length = float(input("Length: "))
width = float(input("Width: "))
area = length * width
print("Area:", area)
```

The algorithm and the Python implementation are related, but they are not the same thing.

## 2. Analyze a Problem Statement

Before coding, identify:

1. **Inputs** — what information enters?
2. **Outputs** — what must be produced?
3. **Operations** — what formulas/transformations connect them?
4. **Assumptions/constraints** — what conditions must hold?

This prevents a common beginner error: writing Python before understanding the problem.

## 3. Worked Example: Speed

Problem: calculate speed from distance and time.

```text
Inputs: distance, time
Output: speed
Formula: speed = distance / time
Risk: time = 0
```

Algorithm:

```text
1. Read distance.
2. Read time.
3. Check time is not zero.
4. Calculate distance / time.
5. Display speed and unit.
```

Implementation:

```python
distance = float(input("Enter distance (m): "))
time = float(input("Enter time (s): "))

if time == 0:
    print("Time cannot be zero.")
else:
    speed = distance / time
    print(f"Speed = {speed} m/s")
```

The edge case was considered before the program was written.

## 4. Arithmetic Operators

```text
+   addition
-   subtraction
*   multiplication
/   true division
//  floor division
%   remainder
**  exponentiation
```

Example:

```python
a = 17
b = 5
print(a / b)   # 3.4
print(a // b)  # 3
print(a % b)   # 2
print(a ** 2)  # 289
```

### Predict

Before running:

```python
x = 17
print(x // 5)
print(x % 5)
print(x / 5)
```

Expected:

```text
3
2
3.4
```

## 5. Operator Precedence

```python
result = 2 + 3 * 4
```

means:

```text
2 + (3 × 4) = 14
```

Use parentheses to make important scientific formulas unambiguous.

## 6. Units Matter

If:

```text
Distance = 100 m
Time = 20 s
```

then:

```text
speed = 5 m/s
```

Good variable names can encode units:

```python
distance_m = 100
elapsed_time_s = 20
speed_m_per_s = distance_m / elapsed_time_s
```

A Python calculation can be syntactically correct while the scientific units are wrong.

## 7. Worked Example: Falling Ball

The model is:

```text
h(t) = h0 - 1/2 × g × t²
```

with:

```text
g = 9.8 m/s²
```

Analyze:

```text
Inputs: h0, t
Constant: g
Output: h(t)
```

Algorithm:

```text
1. Read h0.
2. Read t.
3. Set g = 9.8.
4. Calculate h = h0 - 0.5 × g × t².
5. Report h.
6. Test t = 0.
7. Test additional values.
8. Consider whether the model remains physically meaningful if h becomes negative.
```

Function:

```python
def calculate_height(h0, t):
    g = 9.8
    return h0 - 0.5 * g * t ** 2
```

Trace `h0=50`, `t=2`:

```text
h = 50 - 0.5 × 9.8 × 2²
  = 50 - 19.6
  = 30.4
```

## 8. Mathematics vs Scientific Model

If `calculate_height(50, 4)` produces a negative value, Python may be implementing the formula correctly.

The deeper question is:

> Is the mathematical model still physically valid after the ball reaches the ground?

This gives an important distinction:

```text
Programming correctness ≠ scientific model correctness
```

## 9. Worked Example: Constant-Speed Car

A car travels at 20 m/s.

```text
d = v × t
```

Function:

```python
def calculate_car_distance(t):
    speed = 20
    return speed * t
```

Trace:

```text
calculate_car_distance(3)
= 20 × 3
= 60
```

Functions make the algorithm reusable instead of duplicating calculations.

## 10. Testing Strategy

Do not test only the example in the question.

For `calculate_height()`:

```text
normal: h0=50, t=1
normal: h0=50, t=2
boundary: t=0
model-limit: time large enough to reach ground
```

For `calculate_car_distance()`:

```text
normal: t=1
normal: t=3
boundary: t=0
```

## 11. Debugging Strategy

When a result is wrong:

1. reproduce the problem;
2. check the formula;
3. print intermediate values;
4. check parentheses/operator precedence;
5. check units;
6. change one thing at a time;
7. rerun the test.

Example:

```python
print("h0 =", h0)
print("t =", t)
print("h =", h)
```

## 12. Active Learning Challenges

### Challenge 1 — Predict

```python
x = 5
x = x * 2 + 3
x = x // 4
print(x)
```

Show the intermediate values.

### Challenge 2 — Analyze

For kinetic energy:

```text
KE = 1/2 mv²
```

Identify inputs, output, operations, units, and one edge case.

### Challenge 3 — Debug

What is wrong with:

```python
speed = distance / time
if time == 0:
    print("Invalid time")
```

The division occurs before the check.

### Challenge 4 — Design

Write a function for speed. Decide what it should receive and what it should return.

## Summary

Do not jump from a word problem directly into Python. Build the reasoning first:

```text
Understand → Analyze → Algorithm → Trace → Code → Test → Debug → Explain
```

Your code should make your reasoning visible.
