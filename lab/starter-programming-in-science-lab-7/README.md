# Programming in Science - Lab 7
## Non-Square 2D Array Investigation

Lecture 8 explicitly asks to work with non-square arrays and debug them carefully.

### Question(s) 
You are given a rectangular but not square set of physics observations.
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
Use a 2D list with 2 rows and 5 columns or 4 rows and 3 columns.
Print:
•	matrix dimensions in words,
•	every row on a separate line,
•	the last column using a loop or comprehension,
•	a sub-array containing all rows but only the first 3 columns.

```

#### Component B — ID-based modification (50 marks)
```
Students must:
•	choose one row number using d1 % number_of_rows,
•	replace that entire row with a new row whose values are each increased by k,
•	choose one starting column using d2 % 2,
•	print a sliced sub-array from that starting column onward.


```
✅ **Required details** 
```
•	Students must explain how their chosen row and column came from their ID.
•	They must show the old row and the new row side by side.


```
### Run Command

`pytest`
