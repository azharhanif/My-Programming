# Programming in Science - Assignment 3 
Python Scientific Visualization (Based on Lecture 10 and Lecture 11) 

This is the starter project for Programming in Science Assignment 3. Written in Python and tested with Pytest.

**Total 100: Grading** 
```
40% on the submitted code

60% on the post-submission challange

**What is post-submission challange?**

After final code submission there will be an in class code verification challenges built from the submitted project. The challange is designed to fit a 5-10 minute coding task, and will test high-level understanding, not memorization.
```
### Theme
You are a junior science lab assistant studying the motion and signal behavior of a small experimental system.

You will create:

@ a 2D line plot

@ a 2D density-style / distribution visualization

@ a 3D scatter plot

@ a simple animation

Your work must be personalized using your student ID, so each student produces different numerical results and slightly different graphs.

### Part 0 — Student ID Personalization Rules (Required)
Let:

`d1` = second last digit of your student ID
`d2` = last digit of your student ID

Compute:
```
k = (d1 + d2) % 4 + 2
shift = d1 - d2
n_points = 20 + d1
frame_step = d2 + 1
```
Example

If student ID = 2672601:
```
d1 = 0
d2 = 1
k = (0 + 1) % 4 + 2 = 3
shift = 0 - 1 = -1
n_points = 20
frame_step = 2
```
Every student must print these values at the start of the program.

### Component A — Build from the Lecture Examples (50 marks)
This component must follow the style of the lecture examples:
```
- create x and y data
- use plt.plot(...)
- add title and axis labels
- display the plot
- check that data is not empty and lengths match before plotting.
```
#### Task A1 — 2D Line Plot (15 marks)
Write code that:

1.   creates:
```
x = [1, 2, 3, ..., n_points]
y = x squared
```
2. plots x vs y
3. adds:
   - a title
   - x-axis label
   - y-axis label

4.   uses `plt.figure(figsize=(8, 5))`
5.   checks:
     ```
     x is not empty
     len(x) == len(y)
     ```
##### Required output

A clean line graph similar to the Lecture 10 example.

#### Task A2 — Distribution Plot (15 marks) 

Create a list called data_values of at least 30 numeric values representing repeated measurements.

Then:

1. print the first 10 values
2. create either
      - a histogram using Matplotlib, or
      - a density plot if available
3. give the plot a title and labels
#### Required note
Include a short comment in code explaining:

Why this graph helps us understand the distribution of repeated data.

### Component B — Personalized Scientific Visualization Challenge (50 marks)

This component must use your ID values.

#### Task B1 — Personalized 2D Plot (15 marks)

Using the same `x` list, build a new `y2` list using:

`y2 = k * x + shift`

Then:

1.   plot x vs y2
2.   title must include your student ID
3.   title must also include k and shift
4.   use a different line style or marker from Component A
#### Required demonstration

Print the first 5 `(x, y2)` pairs.

#### Task B2 — Personalized 3D Scatter Plot (15 marks)

Using Lecture 11’s 3D plotting idea, create three lists:
```
x = 1 to n_points
y = x + shift
z = k * x
```
Then:

1.   create a 3D scatter plot
2.   label all three axes
3.   title it properly
4.   print the first 5 `(x, y, z)` points for debugging

This directly follows the lecture’s 3D scatter pattern.

#### Task B3 — Personalized Animation (20 marks)

Create a simple line animation based on Lecture 11’s animation pattern.

Use:
```
x = values from 0 to n_points - 1
y = k * x + shift
```
Then:

1.   animate the line being drawn over time
2.   use `FuncAnimation`
3.   reveal the graph gradually
4.   in the update function, advance by `frame_step`

#### Required debug output

Inside the update logic, print:

`Animating frame: ...`

for at least a few frames, as suggested in Lecture 11 debugging guidance.

### Submission Checklist

Submit:

1.   one .py file
2.   screenshots of:
   - Component A line plot
   - Component A distribution plot
   - Component B personalized 2D plot
   - Component B 3D plot

### Run Command

To run the tests, use the following command:

```
pytest
```

