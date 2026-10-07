# Programming in Science — Midterm Practice Test
## Sample Test with Answers

**Time:** 75 minutes  
**Total:** 30 marks  
**Theory:** 15 marks  
**Programming:** 15 marks  
**VS Code:** Allowed  
**pytest:** Not used

---

# Part A — Theory (15 marks)

## Q1 — Types and Conversion (2 marks)

For:

```python
x, y, z = input("Values: ").split()
x = int(x)
y = float(y)
```

If the user enters:

```text
5 2.5 hello
```

state the final type of `x`, `y`, and `z`.

### Answer

```text
x → int
y → float
z → str
```

`input()` and `split()` initially produce strings. Only `x` and `y` are converted.

---

## Q2 — Arithmetic and Built-ins (2 marks)

Without running:

```python
x = -7.8
a = abs(x)
b = int(x)
c = round(x)
```

What are `a`, `b`, and `c`?

### Answer

```text
a = 7.8
b = -7
c = -8
```

---

## Q3 — Conditional Logic (2 marks)

What is printed?

```python
temperature = 0

if temperature > 0:
    print("above")
elif temperature == 0:
    print("exactly")
else:
    print("below")
```

### Answer

```text
exactly
```

---

## Q4 — Loop Trace (2 marks)

What is the final value of `total`?

```python
total = 0

for n in range(1, 7):
    if n % 2 == 0:
        total += n
```

### Answer

Even values are `2, 4, 6`.

```text
total = 12
```

---

## Q5 — String Indexing and Slicing (2 marks)

Given:

```python
word = "COMPUTER"
```

Find:

```python
word[1]
word[-2]
word[1:6:2]
word[::-1]
```

### Answer

```text
O
E
OPT
RETUPMOC
```

---

## Q6 — String Methods and Splitting (2 marks)

What are the values of `a`, `b`, and `c`?

```python
text = "  Red,Green,Blue  "

a = text.strip()
b = a.split(",")
c = "-".join(b)
```

### Answer

```text
a = "Red,Green,Blue"
b = ["Red", "Green", "Blue"]
c = "Red-Green-Blue"
```

---

## Q7 — List Mutation and Aliasing (3 marks)

What is printed?

```python
numbers = [2, 4, 6]
other = numbers

other.append(8)
numbers[0] = 10

print(numbers)
print(other)
```

### Answer

```text
[10, 4, 6, 8]
[10, 4, 6, 8]
```

`other = numbers` makes both names refer to the same list.

---

# Part B — Programming (15 marks)

## Q8 — String Challenge (3.75 marks)

Write:

```python
def clean_code(text):
    ...
```

Return a new string containing:
- only alphabetic characters and digits;
- all letters converted to uppercase.

Examples:

```python
clean_code("Lab-5: Python!") → "LAB5PYTHON"
clean_code("A 1-b") → "A1B"
```

### Answer

```python
def clean_code(text):
    result = ""

    for ch in text:
        if ch.isalnum():
            result += ch.upper()

    return result
```

---

## Q9 — List Challenge (3.75 marks)

Write:

```python
def adjust_measurements(values):
    ...
```

Return a **new list**:
- values below 10 become `10`;
- values from 10 through 20 stay unchanged;
- values above 20 become `20`.

Do not modify the original list.

Example:

```python
adjust_measurements([7, 10, 15, 23])
→ [10, 10, 15, 20]
```

### Answer

```python
def adjust_measurements(values):
    result = []

    for value in values:
        if value < 10:
            result.append(10)
        elif value > 20:
            result.append(20)
        else:
            result.append(value)

    return result
```

---

## Q10 — Loop Challenge (3.75 marks)

Write:

```python
def alternating_total(limit):
    ...
```

Starting at 1:
- add odd numbers;
- subtract even numbers;
- stop immediately when the running total becomes greater than 10 or less than -10;
- return the total.

### Answer

```python
def alternating_total(limit):
    total = 0
    number = 1

    while number <= limit:
        if number % 2 == 1:
            total += number
        else:
            total -= number

        if total > 10 or total < -10:
            break

        number += 1

    return total
```

---

## Q11 — Mixed String + List Challenge (3.75 marks)

Write:

```python
def count_long_words(sentence, limit):
    ...
```

Split the sentence into words and return the number of words whose length is strictly greater than `limit`.

Example:

```python
count_long_words("Python makes programming interesting", 6)
→ 2
```

### Answer

```python
def count_long_words(sentence, limit):
    words = sentence.split()
    count = 0

    for word in words:
        if len(word) > limit:
            count += 1

    return count
```

---

## Practice advice

The exam is not primarily testing whether you remember syntax. For each problem ask:

1. What data do I have?
2. What changes?
3. What stays the same?
4. Do I need a counter or accumulator?
5. Do I need an index?
6. Is the boundary `<`, `<=`, `>`, or `>=`?
7. Am I modifying the original list or creating a new one?
