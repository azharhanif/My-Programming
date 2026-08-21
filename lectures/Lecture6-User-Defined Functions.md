# Lecture 6: User-Defined Functions — Designing Reusable Solutions

## 0. Why functions?

A long program can become difficult to reason about if everything happens in one block.

A function gives a problem a name:

```python
calculate_velocity(distance, time)
```

Now the program communicates its intent.

## 1. Function Anatomy

```python
def calculate_velocity(distance, time):
    return distance / time
```

- `def` defines the function.
- `distance` and `time` are parameters.
- `return` sends a result to the caller.

Calling:

```python
v = calculate_velocity(100, 20)
```

passes `100` and `20` as arguments.

## 2. Trace a Function Call

```python
def double(x):
    return x * 2

a = 5
b = double(a)
```

Trace:

```text
a = 5
double(5)
x = 5
return 10
b = 10
```

The parameter `x` is local to the function.

## 3. `return` vs `print`

Compare:

```python
def square(x):
    print(x * x)
```

with:

```python
def square(x):
    return x * x
```

The second is more reusable:

```python
answer = square(5)
print(answer + 10)
```

A function that returns a value can be composed with other operations.

## 4. Single Responsibility

Weak:

```python
def analyze_temperature():
    # read input
    # validate input
    # calculate average
    # print report
    # write file
```

Better separation:

```python
def read_temperature():
    ...

def calculate_average(values):
    ...

def print_report(average):
    ...
```

Each function has a clearer responsibility.

## 5. Refactoring

Original:

```python
distance = 100
time = 20
velocity = distance / time
print(velocity)

distance = 50
time = 10
velocity = distance / time
print(velocity)
```

Refactor:

```python
def calculate_velocity(distance, time):
    return distance / time

print(calculate_velocity(100, 20))
print(calculate_velocity(50, 10))
```

The behavior is preserved while repetition is reduced.

## 6. Function Contracts

For each function, be able to state:

```text
Input:
Output:
Assumptions:
Possible invalid input:
```

Example:

```python
def calculate_velocity(distance, time):
    return distance / time
```

Contract:

```text
Input: numeric distance and time
Output: velocity
Assumption: time != 0
```

This makes debugging much easier.

## 7. Open/Closed Principle — Use Carefully

The original course introduces Open/Closed. The important beginner interpretation is:

> Prefer adding a new function for a genuinely new operation rather than repeatedly making one function more complicated.

Avoid turning one function into:

```python
if operation == "area":
...
elif operation == "volume":
...
elif operation == "speed":
...
elif operation == "temperature":
...
```

unless that design is actually appropriate.

## 8. Active-Learning Questions

1. What is the difference between a parameter and an argument?
2. Why is `return` usually more reusable than `print`?
3. What should a function's name communicate?
4. When should a large function be split?
5. What assumptions belong in a function contract?

## 9. Challenge

Create:

```python
def calculate_kinetic_energy(mass, velocity):
    ...
```

Then create:

```python
def calculate_momentum(mass, velocity):
    ...
```

Finally write a short main program that calls both functions.

Do not duplicate the formulas or mix input/output responsibilities into the calculation functions.
