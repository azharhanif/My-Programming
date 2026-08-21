# Programming in Science — Assignment 3
## Scientific Visualization

**Total: 100 marks**  
**Submitted code: 40 marks**  
**Post-submission code-verification challenge: 60 marks**

## Theme

You are a junior science lab assistant studying motion and signal behavior.

Your program will produce:

- a 2D line plot;
- a distribution visualization;
- a 3D scatter plot;
- a simple animation.

This assignment builds directly on Lectures 10–11.

---

# Part 0 — Student ID personalization

Let:

```text
d1 = second-last digit
d2 = last digit

k = (d1 + d2) % 4 + 2
shift = d1 - d2
n_points = 20 + d1
frame_step = d2 + 1
```

Print these values.

---

# Component A — Lecture-based visualization

## A1 — 2D line plot (15)

Create:

```python
x = [1, 2, ..., n_points]
y = [value ** 2 for value in x]
```

Plot with:

```python
plt.figure(figsize=(8,5))
```

Add title and axis labels.

Validate that the data is non-empty and lengths match.

---

## A2 — Distribution (15)

Create at least 30 numeric measurement values.

Print the first 10.

Create a histogram or density-style plot.

In a comment explain why the visualization helps interpret repeated measurements.

---

# Component B — Personalized challenge

## B1 — Personalized 2D plot (15)

Using the same x:

```text
y2 = k*x + shift
```

Plot it with a different style/marker.

The title must include:

- student ID;
- k;
- shift.

Print the first five `(x, y2)` pairs.

---

## B2 — 3D scatter (15)

Create:

```text
x = 1 ... n_points
y = x + shift
z = k*x
```

Plot a 3D scatter.

Label all axes.

Print the first five points.

---

## B3 — Animation (20)

Use:

```text
x = 0 ... n_points-1
y = k*x + shift
```

Use `FuncAnimation`.

Reveal the line gradually.

The update function should advance by:

```text
frame_step
```

Print:

```text
Animating frame: ...
```

for debugging.

---

# Required scientific interpretation

For each major visualization, include a short comment explaining what the graph communicates.

A technically correct graph with no meaningful interpretation is incomplete scientific programming.

---

# Submission

Submit:

- one `.py` file;
- four screenshots;
- comments explaining design choices;
- required ID values;
- post-submission challenge readiness.

No plot should be submitted without labeled axes and a meaningful title.
