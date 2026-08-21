# Programming in Science — Lab 6
## Temperature Grid Explorer

**Estimated time:** 75–90 minutes

### Learning objectives
- represent a scientific grid as a list of lists;
- reason about row and column indexes;
- slice rows and columns;
- avoid aliasing mistakes;
- modify selected rows/columns safely.

### Personalization

```text
d1 = last digit of student ID
d2 = second-last digit
k = (d1 + d2) % 4 + 2
shift = d1 - d2
rows_keep = (d1 % 2) + 2
```

Print these values.

---

## Part A — Explore the grid

Use a hard-coded matrix with at least 3 rows and 4 columns.

Print:

1. entire matrix;
2. one specified element;
3. first two rows;
4. first column;
5. upper-left 2×2 sub-array.

Before coding, draw the row/column indexes.

---

## Part B — Personalize one row

Choose:

```python
row_index = d1 % len(matrix)
```

Add `shift` to every value in that row.

Print:

- row index;
- old row;
- new row;
- matrix before and after.

---

## Part C — Personalize one column

Choose:

```python
column_index = d2 % len(matrix[0])
```

Multiply every value in that column by `k`.

Print the chosen column index and changed values.

---

## Part D — Sub-array

Create a sub-array containing:

```text
first rows_keep rows
first k columns
```

Do not assume `k` is smaller than the number of columns; handle the situation safely.

---

## Part E — Aliasing trap

Predict:

```python
grid = [[1, 2], [3, 4]]
copy_grid = grid[:]

copy_grid[0][0] = 99

print(grid)
```

Explain why slicing the outer list does not create independent inner lists.

---

## Part F — Challenge

Write:

```python
def column_values(matrix, column):
    ...
```

Return the selected column as a new list.

Then write:

```python
def add_to_row(matrix, row, amount):
    ...
```

Do not silently change the wrong row.

Explain how you prevent index errors.
