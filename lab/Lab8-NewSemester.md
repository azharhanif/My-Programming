# Programming in Science — Lab 8
## Reading and Analyzing Wave Data from CSV

**Estimated time:** 80–95 minutes

This is the transition from in-memory data to external scientific data.

### Personalization

```text
d1 = last digit
d2 = second-last digit
k = (d1 + d2) % 4 + 2
shift = d1 - d2
rows_keep = (d1 % 2) + 2
```

---

## Part A — Read oscillatory-wave data

Write:

```python
def read_oscillatory_wave_data(filename):
    ...
```

The CSV contains:

```text
length,amplitude
```

Read the data and compute:

- mean amplitude;
- maximum amplitude.

### Think first

What type does `csv.reader` give you?

Why can you not immediately calculate:

```python
sum(amplitudes)
```

if the values came directly from a CSV file?

---

## Part B — Read standing-wave data

Write:

```python
def read_standing_wave_data(filename):
    ...
```

The CSV contains:

```text
length,tension
```

Use:

\[
v = \sqrt{T/\mu}
\]

with:

```text
μ = 1
```

Compute the wave speed for each row.

---

## Part C — Debugging challenge

A student wrote:

```python
for row in reader:
    amplitude = row[1]
    total += amplitude
```

What is wrong?

Fix it and explain the conversion.

---

## Part D — Personalized data

Create an oscillatory CSV containing:

```text
5 + d2
```

rows.

Add `shift` to every amplitude.

Compute new mean and maximum.

Create a standing-wave CSV containing:

```text
4 + rows_keep
```

rows.

Multiply every tension by `k` and compute new wave speeds.

Filenames must include the student ID.

---

## Part E — File safety

What should happen if:

- the file does not exist?
- a row is missing a value?
- a numeric field contains `"abc"`?

You do not have to build full exception handling yet, but explain how your program should respond.

---

## Part F — Challenge

Write a reusable helper:

```python
def read_numeric_column(filename, column_index):
    ...
```

Return a list of numeric values from one CSV column.

Then use it to simplify your analysis.

Explain how this demonstrates DRY.
