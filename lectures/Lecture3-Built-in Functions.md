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
