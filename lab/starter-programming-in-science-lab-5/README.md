# Programming in Science - Lab 5 
## Sensor List Builder and Calibrator

Lecture 7 introduces lists, indexing, slicing, DRY, arithmetic on lists, sum(), list comprehensions, zip(), and collecting multiple user inputs into a list. 

### Question(s) 
A student is recording simple sensor readings from a lab bench and building a calibration list.
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
#### Build from the lecture 7 examples (50 marks)
```
Write a program that:
•	asks the user how many readings they will enter,
•	stores the readings in a list,
•	prints:
o	the full list,
o	the first reading,
o	the last reading,
o	the slice from index 1 to index 3 if it exists,
o	the sum of the list.

```
✅ **Required details**
```
•	Must use a loop to collect values one by one.

•	Must handle the case where the list is empty.

•	Must label every printed result clearly.
```
#### Component B — ID-based modification (50 marks)
```
Using the same list:
•	create a second list where every reading is increased by shift,
•	create a third list where every reading is multiplied by k,
•	print the element-wise sum of the original list and the shifted list using zip().

Student-specific variation
Because shift and k depend on the student ID, outputs differ for every student

```
✅ **Required details** Use nested `while` loops to build the pattern.
```
•	Do not overwrite the original list.

•	Print all three lists with labels.

•	If the list lengths do not match for any reason, explain why zip() still works the way it does.
```
### Run Command

`pytest`
