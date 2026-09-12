# Lab 4 --- Iterative Logic: Loops With Control

## Programming in Science

### Learning sequence

> **Understand → Predict → Trace → Code → Run → Test → Debug → Explain →
> Modify**

## Lab Goal

In this lab you will learn to use loops to repeat a calculation while
maintaining control over:

-   the sequence of values;
-   the stopping boundary;
-   the progress variable;
-   `break`;
-   `continue`;
-   floating-point sampling.

The important question throughout this lab is:

> **Do I know the sequence of repetitions, or am I waiting for a
> condition?**

**Do not use pytest for this lab.**

------------------------------------------------------------------------

# Part 1 --- Predict Before You Run

Consider:

``` python
total = 0

for i in range(1, 5):
    total += i

print(total)
```

## Task 1A --- Predict

Without running the program, complete this table:

    i   total before   total after
  --- -------------- -------------
    1              ?             ?
    2              ?             ?
    3              ?             ?
    4              ?             ?

Then predict the final output.

### Question

Why does the loop not use `i = 5`?

------------------------------------------------------------------------

# Part 2 --- Range Is a Boundary, Not a Guess

Study these three loops:

``` python
range(5)
```

``` python
range(1, 5)
```

``` python
range(2, 10, 2)
```

## Task 2A --- Predict the values

Write the exact sequence produced by each:

``` text
range(5)        → __________________
range(1, 5)     → __________________
range(2, 10, 2) → __________________
```

## Task 2B --- Write the loops

Write a `for` loop that prints:

### Challenge 1

``` text
0
1
2
3
4
```

### Challenge 2

``` text
3
4
5
6
7
```

### Challenge 3

``` text
2
4
6
8
10
```

### Before running

For each loop answer:

1.  What is the first value?
2.  What is the stopping boundary?
3.  What is the step?

------------------------------------------------------------------------

# Part 3 --- Trace an Accumulator

Create:

``` python
total = 0

for i in range(1, 6):
    total += i

print(total)
```

## Task 3A --- Trace

Complete:

    i   total before   `total += i`   total after
  --- -------------- -------------- -------------
    1                               
    2                               
    3                               
    4                               
    5                               

Predict the output before running.

## Task 3B --- Modify

Change the program so that it adds only:

``` text
2 + 4 + 6 + 8 + 10
```

### Explain

What did you change in `range()`?

------------------------------------------------------------------------

# Part 4 --- Loop Through Each Item

Consider:

``` python
measurements = [12.1, 11.8, 12.5]

for measurement in measurements:
    print(measurement)
```

## Task 4A --- Predict

What will be printed?

## Task 4B --- Modify

Change the program so that it prints each measurement followed by:

``` text
units
```

For example:

``` text
12.1 units
```

### Question

Why is:

``` python
for measurement in measurements:
```

often clearer than using an index when you do not need the position?

------------------------------------------------------------------------

# Part 5 --- While Loops and the Progress Variable

Study:

``` python
time = 0

while time <= 10:
    print(time)
    time += 1
```

## Task 5A --- Trace

Complete the first several iterations:

    time at start  condition `time <= 10`    printed value   time after
  --------------- ------------------------ --------------- ------------
                0                                          
                1                                          
                2                                          
                3                                          

Continue until the loop stops.

## Task 5B --- Predict

How many values will be printed?

## Task 5C --- Explain

What is the **progress variable**?

Why does the loop eventually stop?

------------------------------------------------------------------------

# Part 6 --- Debug an Infinite Loop

Consider this program:

``` python
x = 0

while x < 10:
    print(x)
```

## Task 6A --- Predict

Will this loop stop?

Explain your prediction before running it.

## Task 6B --- Debug

Identify the missing statement.

Rewrite the loop so that it terminates.

### Rule

Do not simply copy the answer from another student.

Be able to explain:

> Which variable changes, and why does that change move the loop toward
> termination?

------------------------------------------------------------------------

# Part 7 --- Break and Continue

Study:

``` python
values = [3, -1, 5, 0, 8]

for value in values:
    if value < 0:
        continue

    if value == 0:
        break

    print(value)
```

## Task 7A --- Trace

Complete this table:

    value  negative?   zero?  action
  ------- ----------- ------- --------
        3                     
       -1                     
        5                     
        0                     
        8                     

## Task 7B --- Predict

What will the program print?

## Task 7C --- Explain

In your own words:

-   What does `continue` do?
-   What does `break` do?
-   Why is `8` never printed?

------------------------------------------------------------------------

# Part 8 --- Modify the Control Logic

Start with:

``` python
values = [3, -1, 5, 0, 8]

for value in values:
    if value < 0:
        continue

    if value == 0:
        break

    print(value)
```

## Task 8A

Modify the program so that it:

-   ignores negative values;
-   stops at zero;
-   prints every positive value before zero.

## Task 8B

Modify it again so that instead of printing the values, it calculates
their sum.

Before running, predict the result.

------------------------------------------------------------------------

# Part 9 --- Scientific Sampling

Consider:

``` python
time = 0

while time <= 5:
    height = 100 - 4.9 * time ** 2
    print(time, height)
    time += 0.5
```

## Task 9A --- Understand

Answer before running:

1.  What is the starting time?
2.  What is the ending boundary?
3.  What is the sampling interval?
4.  Which variable controls termination?
5.  What is calculated at each time?

## Task 9B --- Predict

Calculate the height manually for:

``` text
time = 0
time = 0.5
time = 1.0
```

Then run the program and compare.

## Task 9C --- Modify

Change the program so the sampling interval is:

``` text
0.25
```

How does this affect the number of samples?

------------------------------------------------------------------------

# Part 10 --- Floating-Point Loop Warning

Study:

``` python
x = 0.0

while x != 1.0:
    x += 0.1
```

## Task 10A --- Think

Should this loop reach exactly `1.0`?

Explain your prediction.

**Do not leave a potentially non-terminating loop running
indefinitely.**

If you test it, stop it quickly with:

``` text
Ctrl + C
```

## Task 10B --- Safer Design

Use an integer counter instead:

``` python
for step in range(11):
    x = step * 0.1
    print(x)
```

### Question

Why is the integer-counter approach safer for this type of sampling?

------------------------------------------------------------------------

# Part 11 --- Main Challenge

Given:

``` python
measurements = [12.4, -1.0, 13.2, 0.0, 14.1]
```

Write a program that:

1.  ignores negative values;
2.  stops when it reaches zero;
3.  computes the sum of valid positive values;
4.  reports how many values were included.

## Step 11A --- Predict

Before writing the program, predict:

``` text
sum = ?
number included = ?
```

## Step 11B --- Design

Answer:

1.  Should you use `for` or `while`?
2.  Where should `continue` be used?
3.  Where should `break` be used?
4.  What variables do you need?
5.  What does each variable represent?

## Step 11C --- Code

Write the program.

## Step 11D --- Run

Run your program and compare the result with your prediction.

## Step 11E --- Explain

Explain your loop to a partner without reading the code line by line.

------------------------------------------------------------------------

# Part 12 --- Challenge Modification

Modify the main challenge so that it also reports the **largest valid
positive measurement**.

For:

``` python
measurements = [12.4, -1.0, 13.2, 0.0, 14.1]
```

your result should identify:

``` text
largest = 13.2
```

### Important

Do not sort the list.

The purpose is to practice reasoning through the values one at a time.

------------------------------------------------------------------------

# Part 13 --- Debugging Challenge

The following program is supposed to calculate the sum of positive
measurements before zero:

``` python
measurements = [12.4, -1.0, 13.2, 0.0, 14.1]

total = 0

for measurement in measurements:
    if measurement < 0:
        break

    if measurement == 0:
        continue

    total += measurement

print(total)
```

## Your job

Do not immediately rewrite the program.

First identify:

1.  What does the programmer want the program to do?
2.  What happens when the value is `-1.0`?
3.  What should happen when the value is `-1.0`?
4.  What happens when the value is `0.0`?
5.  What should happen when the value is `0.0`?
6.  Which control statement is in the wrong place?
7.  How would you fix it?

Then run the corrected program.

------------------------------------------------------------------------

# Final Reflection

Answer these questions in your own words.

### 1. `for` vs `while`

When is a `for` loop a natural choice?

When is a `while` loop a natural choice?

### 2. Range

For:

``` python
range(2, 10, 2)
```

identify:

-   first value;
-   stopping boundary;
-   step.

### 3. Progress

What is a progress variable?

### 4. Infinite loops

What can cause a `while` loop to continue forever?

### 5. Control

What is the difference between:

``` python
break
```

and:

``` python
continue
```

### 6. Floating point

Why can this be dangerous?

``` python
while x != 1.0:
```

------------------------------------------------------------------------

# Submission Checklist

Before submitting, make sure you can:

-   [ ] trace a `for` loop;
-   [ ] explain `range()` boundaries;
-   [ ] loop through each item in a list;
-   [ ] identify the progress variable in a `while` loop;
-   [ ] identify and fix an infinite loop;
-   [ ] explain `break`;
-   [ ] explain `continue`;
-   [ ] trace a loop containing `break` and `continue`;
-   [ ] recognize the danger of floating-point equality;
-   [ ] predict a result before running code;
-   [ ] explain why your chosen loop structure makes sense.

## Final Principle

> **A loop is not just repetition. It is controlled repetition.**

Before writing a loop, ask:

> **What changes each iteration, and why will the loop eventually
> stop?**
