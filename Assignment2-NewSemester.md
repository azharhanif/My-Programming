# Programming in Science — Assignment 2
## Lists, Slicing, Vector Operations, and Matrices

**Total: 100 marks**  
**Submitted code: 40 marks**  
**Post-submission challenge: 60 marks**

## Purpose

This assignment moves from individual values to collections.

For every question:

1. implement the function;
2. explain inputs, outputs, and algorithm;
3. include normal and boundary cases;
4. write automated tests;
5. be prepared for a short code-verification modification.

---

# Q1 — Remove Duplicates and Sort

```python
def unique_sorted(numbers):
    ...
```

Return a sorted list containing each value once.

Example:

```text
[4, 2, 4, 1, 2] → [1, 2, 4]
```

Explain whether your solution preserves the original list.

---

# Q2 — Cumulative Sum

```python
def cumulative_sum(numbers):
    ...
```

Return a new list.

Example:

```text
[2, 3, 5] → [2, 5, 10]
```

Do not modify the input list.

---

# Q3 — Every Nth Element

```python
def every_nth(values, n):
    ...
```

Return every `n`th element.

Define and document what happens when:

```text
n <= 0
n > len(values)
```

---

# Q4 — Dot Product

```python
def dot_product(a, b):
    ...
```

For:

```text
[1,2,3]
[4,5,6]
```

return:

```text
32
```

Validate equal lengths.

---

# Q5 — Matrix Multiplication

Implement:

```python
def matrix_multiply(A, B):
    ...
```

The number of columns in `A` must equal the number of rows in `B`.

Example:

```text
A = 2×3
B = 3×2
result = 2×2
```

Explain why the dimensions must match.

### Strong requirement

Do not use NumPy matrix multiplication. Implement the algorithm using lists and loops.

---

# Post-submission preparation

Be prepared to modify one function in 5–10 minutes.

Examples:

- remove duplicates while preserving first-occurrence order;
- cumulative sum starting from a specified initial value;
- every nth element starting from a specified index;
- dot product with validation;
- matrix multiplication dimension error handling.
