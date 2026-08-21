# Programming in Science — Lab 2
## Algorithms, Scientific Formulas, Functions, Testing

**Estimated time:** 75–90 minutes  
**Starter:** `starter-programming-in-science-lab-2`  


## Learning objectives

By the end of this lab you should be able to:

- analyze a scientific problem before coding;
- write a short algorithm;
- translate a formula into Python;
- write reusable functions;
- trace a numerical calculation;
- test boundary cases;
- distinguish mathematical correctness from model validity;
- debug using intermediate values.

## Part 0 — Read the Starter Code and Tests

Open `Lab2.py` and use the examples in this handout for manual testing.

You must implement:

```python
def calculate_height(h0, t):
```

and:

```python
def calculate_car_distance(t):
```

### Before coding, answer

1. What does each function receive?
2. What should each function return?
3. What constant is needed for the falling-ball problem?
4. What examples in the test file give you expected results?
5. What edge case is explicitly tested?

## Part 1 — Falling Ball: Algorithm First

The model is:

```text
h(t) = h0 - 1/2 × g × t²
```

with:

```text
g = 9.8 m/s²
```

### Task 1 — Write the algorithm

Before Python, write 4–6 plain-language steps.

### Task 2 — Trace

For:

```text
h0 = 50
 t = 2
```

show the calculation step by step.

Expected result:

```text
30.4 m
```

### Task 3 — Implement

Write:

```python
def calculate_height(h0, t):
```

It must return the calculated height.

## Part 2 — Test and Explain

Run:

```text
Run the program and compare its output with your predicted results.
```

The supplied tests include:

```text
50 m at 1 s → 45.1 m
50 m at 2 s → 30.4 m
50 m at 3 s → 5.9 m
50 m at 0 s → 50 m
```

### Explain

Why is `t = 0` a particularly useful test?

## Part 3 — Constant-Speed Car

A car travels at 20 m/s.

Formula:

```text
d = v × t
```

### Before coding

Identify:

- input;
- constant;
- operation;
- output;
- unit.

Then implement:

```python
def calculate_car_distance(t):
```

The function should return the distance in meters.

## Part 4 — Predict Before Running

Predict:

```python
print(calculate_car_distance(3))
```

Then run the test suite.

## Part 5 — Debugging Challenge

Suppose a student writes:

```python
def calculate_height(h0, t):
    g = 9.8
    return h0 - 0.5 * g * t ** 2

print(calculate_height(50, 2))
```

This is correct for the supplied mathematical model.

Now suppose another student writes:

```python
def calculate_height(h0, t):
    g = 9.8
    return h0 - 0.5 * g * t * 2
```

### Questions

1. What is different?
2. Why does `** 2` matter?
3. What result would the second version give for `50, 2`?
4. How would you detect the error by tracing rather than guessing?

## Part 6 — Scientific Model Challenge

Try:

```python
calculate_height(50, 4)
```

If the answer is negative, should you immediately change the formula?

Discuss:

> Is the Python calculation wrong, or might the physical model have reached its domain limit?

The purpose is to distinguish:

```text
programming correctness
```

from:

```text
scientific model correctness
```

## Part 7 — Extension Challenge

Create a new function in your own file:

```python
def calculate_average_speed(distance, time):
```

Requirements:

- return `distance / time`;
- handle `time == 0` sensibly;
- write at least three tests;
- include a zero-time test.

You may choose whether to return a special value or raise an exception, but document your choice.

## Part 8 — Explain Your Code

Choose one function and answer:

1. What are its inputs?
2. What does it return?
3. What formula does it implement?
4. What assumption does the formula make?
5. What is one edge case?
6. Which test gives you the most confidence and why?

## Responsible AI activity

If you use AI, ask it to review your algorithm or explain a failing test. Do not ask it to replace the entire reasoning process.

Verify any suggestion by running your tests and explain one suggestion you accepted or rejected.

## Submission checklist

- [ ] algorithm for falling ball
- [ ] trace for `h0=50, t=2`
- [ ] `calculate_height()` implemented
- [ ] tests pass
- [ ] `calculate_car_distance()` implemented
- [ ] debugging challenge answered
- [ ] model-limit discussion completed
- [ ] extension function/tests attempted
- [ ] explanation completed

## Suggested grading

| Component | Marks |
|---|---:|
| Problem analysis/algorithm | 15 |
| Falling-ball implementation | 20 |
| Trace and testing | 15 |
| Car-distance implementation | 15 |
| Debugging challenge | 10 |
| Scientific model discussion | 5 |
| Extension + tests | 10 |
| Explanation/AI reflection | 10 |
| **Total** | **100** |
