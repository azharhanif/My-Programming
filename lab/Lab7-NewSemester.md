# Programming in Science — Lab 7
## Non-Square 2D Array Investigation

**Estimated time:** 75–90 minutes

This lab deliberately uses a rectangular, non-square dataset because many real scientific datasets are not square.

### Personalization

Use:

```text
d1 = last digit
d2 = second-last digit
k = (d1 + d2) % 4 + 2
shift = d1 - d2
```

---

## Part A — Dimensions and structure

Use either:

- 2 rows × 5 columns, or
- 4 rows × 3 columns.

Print:

- number of rows;
- number of columns;
- every row separately;
- last column;
- first three columns of every row.

### Important
Do not assume:

```python
len(matrix) == len(matrix[0])
```

That would be true only for a square matrix.

---

## Part B — ID-selected row

Choose:

```python
row = d1 % len(matrix)
```

Create a new version of that row where every value is increased by `k`.

Print old and new rows side by side.

Explain exactly how the student ID determined the row.

---

## Part C — Slicing challenge

Choose:

```python
start_column = d2 % 2
```

Print all rows from `start_column` onward.

Explain the difference between:

```python
row[start_column:]
```

and:

```python
matrix[start_column:]
```

---

## Part D — Debugging

Find the error:

```python
for column in range(len(matrix)):
    print(matrix[0][column])
```

This code is not necessarily safe for a rectangular matrix.

Explain why.

Rewrite it to extract the first row correctly.

---

## Part E — Design challenge

Write:

```python
def dimensions(matrix):
    ...
```

returning:

```text
(rows, columns)
```

and:

```python
def last_column(matrix):
    ...
```

Return the values as a new list.

Test with both a 2×5 and a 4×3 matrix.
