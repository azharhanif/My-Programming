# Lecture 8: Two-Dimensional Arrays and Slicing

## 0. Why a 2D structure?

A list represents a sequence.

A 2D list represents a grid:

```text
row 0:  1 2 3
row 1:  4 5 6
row 2:  7 8 9
```

In Python this is commonly represented as a list of lists.

## 1. Indexing Requires Two Decisions

```python
matrix[1][2]
```

means:

```text
row 1 → [4,5,6]
column 2 → 6
```

Always identify the row first, then the column.

## 2. Predict Before Running

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix[0][1] = 20
print(matrix)
```

Predict the complete matrix.

## 3. Nested Loops

```python
for row in matrix:
    for value in row:
        print(value)
```

This is often the clearest way to visit every element.

If indices are needed:

```python
for r in range(len(matrix)):
    for c in range(len(matrix[r])):
        print(r, c, matrix[r][c])
```

## 4. Row vs Column

A row is easy:

```python
matrix[1]
```

A column requires visiting each row:

```python
column = [row[1] for row in matrix]
```

This distinction is fundamental.

## 5. Slicing

Rows:

```python
matrix[:2]
```

First two rows.

Columns:

```python
[row[1:3] for row in matrix]
```

Columns 1 and 2 from every row.

Submatrix:

```python
[row[:2] for row in matrix[:2]]
```

## 6. A Common Conceptual Trap

This:

```python
sub = matrix[:2]
```

creates a new outer list, but its rows still refer to the original row lists.

Students should distinguish:

```text
new outer list
```

from:

```text
independent deep copy of every row
```

## 7. Rectangular Matrices

Do not assume:

```python
len(matrix) == len(matrix[0])
```

A matrix can be:

```python
[
    [1, 2, 3, 4],
    [5, 6, 7, 8]
]
```

It has 2 rows and 4 columns.

## 8. Scientific Example

Suppose rows represent experiments and columns represent measurements:

```python
data = [
    [20.1, 20.4, 20.2],
    [21.0, 20.8, 21.1],
    [19.9, 20.0, 20.2]
]
```

A useful design question is:

> Does `data[1]` represent a measurement, an experiment, or a feature vector?

The answer depends on the data model you choose.

## 9. Active-Learning Questions

1. What does `matrix[2][1]` mean?
2. How do you extract a column?
3. Why does a nested loop have two levels?
4. What happens if the matrix has no rows?
5. Why might a rectangular matrix break code that assumes a square matrix?

## 10. Challenge

Given a rectangular matrix, write functions that return:

```python
row_sum(matrix, row_index)
column_sum(matrix, column_index)
```

Then write:

```python
find_largest(matrix)
```

that searches every element.

Test:

- normal matrix;
- one-row matrix;
- one-column matrix;
- empty matrix.
