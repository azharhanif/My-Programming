# Programming in Science — Lab 5
## Sensor List Builder and Calibrator

**Estimated time:** 75–90 minutes

This lab uses the existing student-ID personalization idea, but the emphasis is now on understanding lists rather than merely producing different answers.

### Personalization

Let:

```text
d1 = last digit of student ID
d2 = second-last digit
k = (d1 + d2) % 4 + 2
shift = d1 - d2
```

Print these values before your program starts.

---

## Part A — Build the measurement list

Ask how many sensor readings the user will enter.

Collect the readings one at a time using a loop.

Print:

- full list;
- first reading, if present;
- last reading, if present;
- slice from index 1 through index 3 when possible;
- sum.

### Before coding
What should happen if the user enters `0` readings?

Do not allow `readings[0]` to execute on an empty list.

---

## Part B — Transform without destroying the original

Create:

```python
shifted = [...]
scaled = [...]
```

where:

```text
shifted[i] = readings[i] + shift
scaled[i] = readings[i] * k
```

The original list must remain unchanged.

Use a loop or list comprehension.

---

## Part C — zip()

Create an element-wise sum of:

```text
readings
shifted
```

using `zip()`.

Explain what `zip()` does if the two lists have different lengths.

---

## Part D — Debugging

Consider:

```python
readings = [10, 20, 30]
shifted = readings

for i in range(len(readings)):
    shifted[i] += shift
```

Why does this unexpectedly modify `readings`?

Fix it.

---

## Part E — Challenge

Write:

```python
def calibrate(readings, shift, k):
    ...
```

It should return **three new lists**:

```text
shifted
scaled
combined
```

where `combined` is the element-wise sum of original and shifted values.

Do not modify the original list.

---

## Explain

Why is returning new lists preferable here to repeatedly overwriting the original measurements?

Submit code and short explanations.
