# Sample Solution — Midterm Test A

**Total: 30 marks | Time: 75 minutes**

## Part A — Theory

### Q1 — 2 marks

```text
a = 12       int
b = 4.5      float
c = "hello"  str
```

### Q2 — 2 marks

```text
12.7
-12
-13
```

### Q3 — 2 marks

Original output:

```text
B
```

With `if score >= 70:`:

```text
A
```

### Q4 — 2 marks

`range(2, 10, 2)` → `2, 4, 6, 8`

Skip 6:

```text
2 + 4 + 8 = 14
```

### Q5 — 2 marks

```text
P
N
YTHO
PTO
NOHTYP
```

### Q6 — 2 marks

```text
words = ["red", "green", "blue"]
result = "red|green|blue"
```

### Q7 — 3 marks

After append:

```text
[3, 5, 7, 9]
```

Then index 1 becomes `3 + 7 = 10`:

```text
[3, 10, 7, 9]
```

`append()` adds a new item to the end. Index assignment replaces an existing item.

---

# Part B — Programming

## Q8 — 3.75 marks

```python
def extract_digits(text):
    result = ""

    for ch in text:
        if ch.isdigit():
            result += ch

    return result
```

Marking:
- 1.0 traversal
- 1.5 correct digit test
- 0.75 result construction
- 0.5 return

## Q9 — 3.75 marks

```python
def cap_values(numbers, maximum):
    result = []

    for number in numbers:
        if number > maximum:
            result.append(maximum)
        else:
            result.append(number)

    return result
```

Marking:
- 1.0 new list
- 1.5 correct condition/transformation
- 0.75 preserve other values
- 0.5 return

## Q10 — 3.75 marks

```python
def sum_multiples(limit):
    total = 0

    for number in range(1, limit + 1):
        if number % 3 == 0 and number != 12:
            total += number

    return total
```

Marking:
- 1.0 correct range
- 1.25 divisibility condition
- 0.75 exclusion of 12
- 0.5 accumulator
- 0.25 return

## Q11 — 3.75 marks

```python
def count_words_starting_with(words, letter):
    count = 0

    for word in words:
        if len(word) > 0 and word[0].lower() == letter.lower():
            count += 1

    return count
```

Marking:
- 1.0 list iteration
- 1.0 first-character logic
- 1.0 case-insensitive comparison and empty-word safety
- 0.5 counter
- 0.25 return

Equivalent solutions are fully acceptable.

---


