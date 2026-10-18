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

Explanation
- `print(matrix[1])`

`matrix[1]` selects the second row because Python indexing starts at 0.
```
[4, 5, 6]
```
- `print([row[1] for row in matrix])`
This list comprehension selects the element at index 1 (the second column) from every row.
```
Row	                row[1]
[1, 2, 3]	        2
[4, 5, 6]	        5
[7, 8, 9]	        8
```
Therefore, the result is:
[2, 5, 8]

Key difference: `matrix[1]` selects an entire row, 

while `[row[1] for row in matrix]` selects one element from each row, forming the second column.
## 5. Slicing

Rows:

```python
matrix[:2]

output:
[[1, 2, 3], [4, 5, 6]]
```
Explanation: 

`[:2]` selects rows from the beginning up to, but not including, index 2. Therefore, it selects the first two rows.
 

Columns:

```python
[row[1:3] for row in matrix]

output:
[[2, 3], [5, 6], [8, 9]]

```
Explanation:
- for `row` in matrix visits each `row`.
- `row[1:3]` selects elements at indices 1 and 2 from each `row`.
- The list comprehension collects these slices into a new list.

Submatrix:

```python
[row[:2] for row in matrix[:2]]

output:
[[1, 2], [4, 5]]
```
This selects the top-left `2 x 2` submatrix

Here, `matrix[:2]` selects the first two rows, and 

`row[:2]` selects the first two elements of each selected row.

## 6. A Common Conceptual Trap: Advanced topic

A shallow copy of a 2D list creates a new outer list, but the inner lists are still shared.
#### What happens with sub = matrix[:2]?
Consider this matrix:
```
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

sub = matrix[:2]
```
The expression matrix[:2] creates a new outer list containing the first two rows.
```
print(sub)
```
Output:
```
[[1, 2, 3], [4, 5, 6]]
```
At first glance, sub looks like a separate matrix. However, its inner rows are still shared with matrix.
#### The surprising part: changing an element
Run this code:
```
matrix = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
sub = matrix[:2]
sub[0][0] = 99
print(sub)
print(matrix)
```
Output:
```
[[99, 2, 3], [4, 5, 6]]
[[99, 2, 3], [4, 5, 6], [7, 8, 9]]
```

Why did `matrix` change too?
- `sub[0]` refers to the same inner list as `matrix[0]`.
- `sub[0][0] = 99` modifies that shared inner list.
- Both outer lists therefore show the updated value.
#### But changing an outer-list element behaves differently
Now try:
```
matrix = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
sub = matrix[:2]
sub[0] = [100, 200, 300]
print(sub)
print(matrix)

```
Output:
```
[[100, 200, 300], [4, 5, 6]]
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```
This time, matrix remains unchanged.

Why? The statement `sub[0] = ...` replaces an element in the new outer list. 

It does not modify the original first row.

Compare the two operations:
```
Code	                    What changes?	                            Does matrix change?
sub[0][0] = 99	            An element inside a shared row	            Yes
sub[0] = [100, 200, 300]	A row reference in the new outer list	    No
```
#### How do we make every row independent?
If you want to change sub without affecting matrix, copy each row as well:
```
matrix = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
sub = [row[:] for row in matrix[:2]]
sub[0][0] = 99
print(sub)
print(matrix)
```
Output:
```
[[99, 2, 3], [4, 5, 6]]
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```
Here:
- `matrix[:2]` selects the first two rows.
- `row[:]` creates a separate copy of each selected row.
- Therefore, changing an element in sub does not change the corresponding element in matrix.
  
For a matrix containing only numbers or strings, this is sufficient to make the rows independent.

**The rule to remember:** 
`matrix[:2]` copies the outer list structure, not the inner row lists. 

To independently copy the rows, use `[row[:] for row in matrix[:2]]`.

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

## 8. Blood Glucose Measurements in a Health Science Laboratory

Suppose a health science class conducts three laboratory experiments to measure blood glucose levels (in mmol/L). 

Each experiment records measurements at three different time points.
```
data = [
    [5.2, 5.8, 5.5],  # Experiment 1
    [6.1, 6.4, 6.0],  # Experiment 2
    [4.9, 5.1, 5.0]   # Experiment 3
]
```
In this data model, each row represents one experiment, and each column represents a measurement time point.
For example:
```
Experiment	        Time 1	Time 2	Time 3
Experiment 1	    5.2	    5.8	    5.5
Experiment 2	    6.1	    6.4	    6.0
Experiment 3	    4.9	    5.1	    5.0
```
Now consider:
```
print(data[1])
```
Output:
```
[6.1, 6.4, 6.0]
```
This gives all three glucose measurements from **Experiment 2**.

A useful design question is:
```
Does `data[1]` represent a patient, a laboratory experiment, or a measurement time point?
```
The answer depends on how the data is organized. 

In our example, `data[1]` represents **Experiment 2**, because each row corresponds to one experiment. 

If instead,
- each row represented a patient and
- each column represented a different health indicator (such as glucose level, heart rate, and blood pressure)
- then `data[1]` would represent the second patient's measurements.

**Key lesson:** Before working with a `2D list`, decide what each row and each column represents. 

A clear data model makes your Python code easier to understand, interpret, and maintain.
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
