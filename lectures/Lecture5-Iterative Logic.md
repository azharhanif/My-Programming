# Lecture 5: Iterative Logic — Repetition With Control

## 0. Why loops?

A loop is useful when the same reasoning must be applied repeatedly:

```text
for every measurement
for every time step
until the experiment reaches a target
```

The key design question is:

> **Do I know the sequence of values/repetitions, or am I waiting for a condition?**

## 1. For Loop: Trace It

```python
total = 0

for i in range(1, 5):
    total += i

print(total)
```

Trace:

| i | total before | total after |
|---:|---:|---:|
| 1 | 0 | 1 |
| 2 | 1 | 3 |
| 3 | 3 | 6 |
| 4 | 6 | 10 |

The range stops before `5`.

## 2. Common Range Patterns

```python
range(5)        # 0,1,2,3,4
range(1, 5)     # 1,2,3,4
range(2, 10, 2) # 2,4,6,8
```

Always ask:

> What is the first value? What is the stopping boundary? What is the step?

## 3. For Each Item

```python
measurements = [12.1, 11.8, 12.5]

for measurement in measurements:
    print(measurement)
```

This is often clearer than indexing when the index is not needed.

## 4. While Loop: Identify the Progress Variable

```python
time = 0

while time <= 10:
    print(time)
    time += 1
```

A `while` loop needs a path toward termination.

Ask:

> Which variable changes so that the condition eventually becomes false?

## 5. Infinite Loop Debugging

Bad:

```python
x = 0

while x < 10:
    print(x)
```

`x` never changes.

Correct:

```python
x += 1
```

## 6. Break and Continue

`break` means:

> Stop the loop now.

`continue` means:

> Skip the rest of this iteration and continue with the next one.

Example:

```python
for value in values:
    if value < 0:
        continue

    if value == 0:
        break

    print(value)
```

Trace this with:

```python
values = [3, -1, 5, 0, 8]
```

## 7. Scientific Example: Numerical Sampling

```python
time = 0

while time <= 5:
    height = 100 - 4.9 * time ** 2
    print(time, height)
    time += 0.5
```

Now ask:

- What is the sampling interval?
- How many samples are produced?
- What happens near the boundary?
- Does floating-point arithmetic affect the stopping condition?

## 8. Floating-Point Loop Warning

This can be risky:

```python
x = 0.0

while x != 1.0:
    x += 0.1
```

Floating-point values are not always represented exactly.

A safer design may use an integer counter:

```python
for step in range(11):
    x = step * 0.1
```

## 9. Active-Learning Questions

1. Why does `range(5)` not include 5?
2. What is the progress variable in a `while` loop?
3. What causes an infinite loop?
4. When is `for value in list` clearer than indexing?
5. Why can floating-point equality be dangerous?

## 10. Challenge

Given:

```python
measurements = [12.4, -1.0, 13.2, 0.0, 14.1]
```

write a loop that:

- ignores negative values;
- stops when it reaches zero;
- computes the sum of the valid positive values;
- reports how many values were included.

Before running it, predict the result.
