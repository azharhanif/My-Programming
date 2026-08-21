# Lecture 4: Conditional Statements — Making Decisions

## 0. Why conditions matter

A scientific program often needs to choose what to do:

```text
Is the temperature above the safe limit?
Is the velocity positive?
Is a measurement inside the acceptable range?
Is the denominator zero?
```

An `if` statement turns a Boolean condition into program behavior.

## 1. Predict Before Running

```python
temperature = 20

if temperature > 20:
    print("hot")
elif temperature == 20:
    print("exactly 20")
else:
    print("cold")
```

Predict the output.

Now change `20` to:

```text
19
20
21
```

What changes?

## 2. Comparison Operators

```python
==  !=  >  <  >=  <=
```

Important distinction:

```python
x = 10      # assignment
x == 10     # comparison
```

## 3. Boolean Conditions

```python
temperature = 22
humidity = 40

if temperature > 20 and humidity < 60:
    print("condition acceptable")
```

Think of `and` as requiring both conditions.

```python
if temperature > 30 or humidity > 80:
    print("warning")
```

At least one condition must be true.

```python
if not sensor_available:
    print("Cannot collect data")
```

## 4. Boundary Thinking

Suppose the acceptable temperature range is 18 through 25 inclusive.

Correct:

```python
if 18 <= temperature <= 25:
    print("acceptable")
```

This is clearer than:

```python
if temperature >= 18 and temperature <= 25:
```

Both work, but the first communicates the range directly.

## 5. A Tricky Ordering Problem

Consider:

```python
score = 85

if score >= 50:
    print("pass")
elif score >= 80:
    print("excellent")
```

What prints?

Why does `"excellent"` never print?

The conditions are checked from top to bottom. A condition that is too broad can prevent later branches from being reached.

Correct ordering:

```python
if score >= 80:
    print("excellent")
elif score >= 50:
    print("pass")
else:
    print("fail")
```

## 6. Scientific Decision Example

```python
velocity = -4.2

if velocity > 0:
    direction = "positive"
elif velocity < 0:
    direction = "negative"
else:
    direction = "zero"

print(direction)
```

Separate the **classification** from the output when possible.

## 7. Debugging Conditions

For a complicated condition:

```python
if age >= 18 and has_id and not suspended:
```

temporarily inspect the pieces:

```python
print(age >= 18)
print(has_id)
print(not suspended)
```

This helps locate which assumption failed.

## 8. Active-Learning Questions

1. What is wrong with using `=` instead of `==`?
2. Why does branch order matter?
3. How would you test a condition whose valid range is `0 <= x <= 1`?
4. Why are boundary values especially important?
5. Write a condition for "temperature is below 0 OR above 100."

## 9. Mini Challenge

Ask for a temperature and classify it as:

```text
below freezing       < 0
freezing point       == 0
liquid range         0 < T < 100
boiling point        == 100
above boiling        > 100
```

Test exactly:

```text
-1, 0, 25, 100, 101
```

Explain why these five tests are better than testing only `25`.
