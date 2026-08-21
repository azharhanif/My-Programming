# Programming in Science — Lab 4
## Conditional Reasoning: Valid Days and Scientific Decision Rules

**Estimated time:** 70–85 minutes

### Learning objectives
- build compound conditions;
- distinguish validation from classification;
- understand `if/elif/else` order;
- test boundary values;
- explain why condition order matters.

---

## Part A — Valid Day

A day number is valid when:

```text
1 ≤ day ≤ 7
```

Write:

```python
def day_type(day):
    ...
```

Return:

```text
"Not a proper day number!"
"It is a Weekday!"
"It is a Weekend!"
```

Monday–Friday are weekdays; Saturday–Sunday are weekends.

### Predict before coding

What should happen for:

```text
0
1
5
6
7
8
```

---

## Part B — Day Name

Write:

```python
def day_name(day):
    ...
```

Examples:

```text
2 → "It is a Tuesday!"
7 → "It is a Sunday!"
8 → "Not a proper day number!"
```

You may use `if/elif` or `match` only if it has been covered in class.

---

## Part C — The tricky branch-order problem

Predict the result:

```python
if score >= 50:
    print("Pass")
elif score >= 80:
    print("Excellent")
```

Why will `85` not print `"Excellent"`?

Rewrite it correctly.

---

## Part D — Scientific classification

Write:

```python
def classify_temperature(temp):
    ...
```

Use:

```text
temp < 0       → "Freezing"
0–19           → "Cold"
20–29          → "Moderate"
30 or higher   → "Hot"
```

### Boundary tests
Test:

```text
-1, 0, 19, 20, 29, 30
```

Explain why boundary tests are more valuable than testing only 10, 25, and 40.

---

## Part E — Debugging

Fix:

```python
def classify_temperature(temp):
    if temp < 0:
        return "Freezing"
    elif temp < 20:
        return "Cold"
    elif temp < 30:
        return "Hot"
    elif temp >= 30:
        return "Moderate"
```

The program runs. The problem is logical.

Identify the error and correct it.

---

## Part F — Explain

For one of your functions, identify:

- validation condition;
- classification conditions;
- first boundary value;
- last boundary value;
- one invalid input.

Submit code plus short explanations.
