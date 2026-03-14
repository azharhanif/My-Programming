# Programming in Science - Lab 6
## Temperature Grid Explorer

Lecture 8 focuses on 2D arrays as lists of lists, element access by row/column, row slicing, column extraction via list comprehension, and sub-array creation. 

### Question(s) 
A temperature sensor records values over several days and times. Students explore a 2D temperature grid.
### Scenario 
Each student must compute these three personalization values from their student ID before starting:
```
•	d1 = last digit of student ID

•	d2 = second-last digit of student ID

•	k = (d1 + d2) % 4 + 2

•	shift = d1 - d2

•	rows_keep = (d1 % 2) + 2

Students must include these values at the top of every submission and use them in their code. 

This forces outputs to differ across students.
```
#### Component A: Build from the lecture 8 examples (50 marks)
```
Start from a hard-coded 2D list with at least 3 rows and 4 columns representing temperatures.
Write code that prints:
•	the full matrix,
•	one specific element,
•	the first two rows,
•	the first column,
•	a 2×2 sub-array from the upper-left corner.

```

#### Component B — ID-based modification (50 marks)
```
Students must personalize the grid:
•	add shift to every value in row d1 % number_of_rows,
•	multiply every value in column d2 % number_of_columns by k,
•	create and print a sub-array using:
o	the first rows_keep rows,
o	the first k columns.

```
✅ **Required details** 
```
•	Students must print the matrix before and after modification.
•	They must identify exactly which row and column were changed based on their ID.

```
### Run Command

`pytest`
