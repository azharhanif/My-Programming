# Programming in Science — Assignment 1 (group of 2 allowed)
## Control Flow, Loops, and Functions

**Total: 100 marks**  
**Submitted code: 70 marks**  
**Post-submission challenge: 30 marks**


> **Important:** Pytest is introduced with this assignment. You are now moving from manual testing to automated verification.

## Purpose

This assignment tests whether you can read a requirement, design a small algorithm, implement it, test it, and then modify it.

AI tools may be used as learning partners, but you must understand and explain your submitted code.

---

# General requirement for EACH question

### Task 1 — Code
Implement the required function.

Add a small `main` block that demonstrates the function with meaningful inputs.

### Task 2 — Understanding
In comments, identify:

- inputs;
- output;
- important variables;
- control structure used;
- one boundary case.

### Task 3 — Modification
Make **one meaningful modification** and explain it.

Examples:

- validation;
- changed condition;
- additional feature;
- improved output;
- different input rule.

Do not use programming constructs that have not yet been taught.

---

# Q1 — Number Sign

Write:

```python
def classify_number(number):
    ...
```

Return:

```text
"Positive"
"Negative"
"Zero"
```

Test negative, zero, and positive values.

### Post-submission challenge idea (add this modified function as mod_classify_number(number))
Modify the function to classify numbers into:

```text
negative
zero
small positive
large positive
```

using a threshold chosen during the challenge.

---

# Q2 — Star Pattern

Write:

```python
def print_star_shape(rows):
    ...
```

For:

```text
5
```

print:

```text
*
**
***
****
*****
```

Validate that `rows` is not negative.

### Post-submission challenge idea (add this modified function as mod_print_star_shape(rows))
Reverse the pattern without rewriting the function from scratch.

---

# Q3 — Multiples of 3

Write:

```python
def describe_multiples(limit):
    ...
```

Count from 1 to `limit` using a `while` loop.

For every multiple of 3, print:

```text
Multiple of 3
```

Otherwise print the number.

### Post-submission challenge idea (add this modified function as mod_describe_multiples(limit))
Change the function so that it counts how many multiples of 3 occurred and returns the count.

---

# Q4 — Sum of Even Numbers

Write:

```python
def sum_even(start, end):
    ...
```

Return the sum of all even numbers in the inclusive range.

Examples:

```text
sum_even(1, 10) → 30
sum_even(4, 8) → 18
```

### Required edge cases (add in pytest file)

Test:

```text
start == end
start > end
negative values
```

Explain your chosen behavior when `start > end`.

---

# Submission

Submit:

- one `.py` file;
- required comments;
- pytest tests;

