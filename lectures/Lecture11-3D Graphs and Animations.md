# Lecture 11 — 3D Graphs and Animations

> **New-semester teaching approach:** Explain → Predict → Trace → Code → Run → Debug → Modify → Explain

## Table of Contents

1. [Learning Goals](#learning-goals)
2. [From 2D to 3D Thinking](#from-2d-to-3d-thinking)
3. [Creating 3D Plots with Matplotlib](#creating-3d-plots-with-matplotlib)
4. [3D Scatter Plots](#3d-scatter-plots)
5. [3D Line Plots](#3d-line-plots)
6. [Creating Animations with Matplotlib](#creating-animations-with-matplotlib)
7. [How FuncAnimation Thinks](#how-funcanimation-thinks)
8. [Saving Animations](#saving-animations)
9. [Debugging 3D Graphics and Animations](#debugging-3d-graphics-and-animations)
10. [Active Learning Challenges](#active-learning-challenges)
11. [Key Takeaways](#key-takeaways)

---

# Learning Goals

By the end of this lecture, you should be able to:

- explain why a 3D graph is different from a 2D graph;
- create a 3D scatter plot;
- create a 3D line plot;
- explain the relationship between `x`, `y`, and `z` data;
- explain what `projection='3d'` does;
- create a simple animation using `FuncAnimation`;
- explain the role of a **frame** and an **update function**;
- debug a graph by inspecting the underlying data;
- distinguish a programming/rendering problem from a data problem;
- modify an existing visualization instead of blindly rewriting it.

---

# 1. From 2D to 3D Thinking

In a normal 2D graph, each observation can be represented by:

```text
(x, y)
```

For example:

```python
x = [1, 2, 3, 4]
y = [2, 4, 6, 8]
```

A point is therefore:

```text
(1, 2)
(2, 4)
(3, 6)
(4, 8)
```

A 3D graph adds another coordinate:

```text
(x, y, z)
```

For example:

```python
x = [1, 2, 3, 4]
y = [2, 4, 6, 8]
z = [5, 6, 7, 8]
```

The observations are:

```text
(1, 2, 5)
(2, 4, 6)
(3, 6, 7)
(4, 8, 8)
```

## Think before you run

If:

```python
x = [1, 2, 3]
y = [10, 20, 30]
z = [100, 200, 300]
```

then:

```text
x[1] = 2
y[1] = 20
z[1] = 200
```

represents **one observation**:

```text
(2, 20, 200)
```

The three lists are not three unrelated datasets. They are three coordinates describing the same observations.

### Important rule

For a simple point-by-point 3D plot:

```text
len(x) == len(y) == len(z)
```

should normally be true.

---

# 2. Creating 3D Plots with Matplotlib

The basic structure from the original course material is:

```python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()

ax = fig.add_subplot(
    111,
    projection='3d'
)

ax.scatter(x, y, z)

plt.show()
```

The important line is:

```python
ax = fig.add_subplot(111, projection='3d')
```

It creates a 3D set of axes.

## What does `111` mean?

For now, think of:

```python
111
```

as saying:

```text
1 row
1 column
first plotting area
```

The important new idea for this lecture is:

```python
projection='3d'
```

Without it, the axes are ordinary 2D axes.

---

# 3. 3D Scatter Plots

A scatter plot represents individual observations as points.

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(100)
y = np.random.rand(100)
z = np.random.rand(100)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(x, y, z)

ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')

plt.show()
```

## Read the program before running it

There are four major stages:

```text
1. Create data
       ↓
2. Create figure
       ↓
3. Create 3D axes
       ↓
4. Plot and label data
```

### Predict

Before running:

```python
x = np.random.rand(100)
y = np.random.rand(100)
z = np.random.rand(100)
```

What range of values do you expect?

What happens if you replace `100` with `5`?

---

# 4. A More Meaningful Scientific Example

Random data is useful for learning syntax, but scientific visualization becomes more meaningful when the variables have a relationship.

Consider:

```python
x = np.linspace(0, 10, 100)
y = np.sin(x)
z = np.cos(x)
```

Now each observation is approximately:

```text
(x, sin(x), cos(x))
```

Plot it:

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y = np.sin(x)
z = np.cos(x)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(x, y, z)

ax.set_xlabel('x')
ax.set_ylabel('sin(x)')
ax.set_zlabel('cos(x)')

plt.show()
```

### Why is this better than random data for learning?

Because we know something about the relationship between the variables.

The graph is no longer merely:

> "Here are 100 points."

We can ask:

> "What mathematical relationship generated these points?"

That is the beginning of scientific visualization.

---

# Active Learning Checkpoint 1

Without running the program, answer:

```python
x = np.linspace(0, 2*np.pi, 5)
y = np.sin(x)
z = np.cos(x)
```

### Q1
How many observations are there?

### Q2
What is approximately the first value of `x`?

### Q3
What is approximately the first value of `y`?

### Q4
What is approximately the last value of `x`?

### Q5
Why are `y` and `z` different even though they use the same `x`?

---

# 5. 3D Line Plots

A 3D line connects observations in sequence.

```python
x = np.linspace(0, 10, 100)
y = np.sin(x)
z = np.cos(x)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot(x, y, z)

ax.set_xlabel('x')
ax.set_ylabel('sin(x)')
ax.set_zlabel('cos(x)')

plt.show()
```

Compare:

```python
ax.scatter(x, y, z)
```

with:

```python
ax.plot(x, y, z)
```

### Conceptual difference

**Scatter:**

```text
individual observations
```

**Line:**

```text
ordered observations connected as a path
```

Therefore, choosing between them is a **data/design decision**, not just a syntax decision.

---

# Active Learning Checkpoint 2

Suppose you have measurements of 100 stars.

Would you automatically connect the stars with:

```python
ax.plot(...)
```

Why or why not?

Now suppose you have 100 sequential measurements of the position of a moving object.

Would a line plot make more sense?

Explain.

---

# 6. Creating Animations with Matplotlib

A static graph shows one state of the data.

An animation shows how that state changes.

Matplotlib provides:

```python
FuncAnimation
```

from:

```python
from matplotlib.animation import FuncAnimation
```

The basic idea is:

```text
frame 1 → draw state 1
frame 2 → draw state 2
frame 3 → draw state 3
...
```

---

# 7. The Simplest Animation Model

Consider:

```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

fig, ax = plt.subplots()

line, = ax.plot([], [])

ax.set_xlim(0, 2*np.pi)
ax.set_ylim(-1, 1)
```

At this point:

- `x` contains the horizontal coordinates;
- `y` contains the corresponding sine values;
- `line` is the graphical object that we will update.

---

# 8. The `init()` Function

We can start with an empty line:

```python
def init():
    line.set_data([], [])
    return line,
```

Notice the comma:

```python
return line,
```

This returns a one-element tuple.

The important idea is not the punctuation. It is that the animation framework needs to know which graphical object is being updated.

---

# 9. The `update(frame)` Function

Now:

```python
def update(frame):
    line.set_data(
        x[:frame],
        y[:frame]
    )

    return line,
```

This is the key idea.

If:

```text
frame = 5
```

then:

```python
x[:5]
y[:5]
```

contain the first five observations.

If:

```text
frame = 50
```

then the first fifty observations are displayed.

Therefore:

> **The frame controls how much of the data has been revealed.**

---

# Active Learning Checkpoint 3

What does:

```python
x[:10]
```

mean?

What does:

```python
x[:1]
```

mean?

What does:

```python
x[:len(x)]
```

mean?

Why is slicing useful for an animation?

---

# 10. Creating the Animation

Now:

```python
ani = FuncAnimation(
    fig,
    update,
    frames=len(x),
    init_func=init,
    blit=True
)

plt.show()
```

The important pieces are:

```text
fig
 ↓
the figure being animated

update
 ↓
function called for each frame

frames
 ↓
which frame values are used

init_func
 ↓
initial state

blit
 ↓
optimization for redrawing
```

---

# Complete Sine-Wave Animation

```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

fig, ax = plt.subplots()

line, = ax.plot([], [])

ax.set_xlim(0, 2*np.pi)
ax.set_ylim(-1, 1)

def init():
    line.set_data([], [])
    return line,

def update(frame):
    line.set_data(
        x[:frame],
        y[:frame]
    )
    return line,

ani = FuncAnimation(
    fig,
    update,
    frames=len(x),
    init_func=init,
    blit=True
)

plt.show()
```

---

# Trace the Animation

Imagine:

```text
frame = 1
```

The line contains approximately one point.

Then:

```text
frame = 2
```

Two points.

Then:

```text
frame = 3
```

Three points.

Eventually:

```text
frame = 100
```

The complete sine curve has been displayed.

The animation is therefore not magically "drawing a graph."

It is repeatedly calling:

```python
update(frame)
```

with different frame values.

---

# 11. A Common Debugging Technique

Add:

```python
print("Animating frame:", frame)
```

inside `update()`:

```python
def update(frame):
    print("Animating frame:", frame)

    line.set_data(
        x[:frame],
        y[:frame]
    )

    return line,
```

This allows you to determine whether the animation is actually progressing.

### Important debugging principle

If the animation looks wrong, do not immediately rewrite everything.

First ask:

```text
Are the data correct?
        ↓
Are the frame values changing?
        ↓
Is update() being called?
        ↓
Is the graphical object being updated?
        ↓
Are the axes appropriate?
```

---

# Active Learning Checkpoint 4

Suppose this prints:

```text
Animating frame: 1
Animating frame: 2
Animating frame: 3
...
```

but nothing appears on the graph.

What does that tell you?

It tells you that the animation callback is probably running.

Therefore, the next debugging step should focus on:

- the figure;
- the axes;
- the line object;
- the limits;
- the data being passed to `set_data()`.

Do not immediately blame `FuncAnimation`.

---

# 12. A Deliberate Bug

Consider:

```python
def update(frame):
    line.set_data(
        x[:frame],
        y[frame:]
    )
    return line,
```

Is this correct?

Usually no.

For:

```text
frame = 10
```

we have:

```python
x[:10]
```

but:

```python
y[10:]
```

contains everything from index 10 onward.

The two arrays generally have different lengths.

The intended code is:

```python
line.set_data(
    x[:frame],
    y[:frame]
)
```

---

# Active Learning Checkpoint 5

Find the bug:

```python
def update(frame):
    line.set_data(x[:frame], y[:frame + 1])
    return line,
```

Why can this create mismatched x/y data?

Correct it.

---

# 13. Performance and `blit=True`

The original course material introduces:

```python
blit=True
```

as an optimization.

The basic idea is:

> redraw only the graphical elements that change rather than unnecessarily rebuilding everything.

For a simple line animation, this can improve performance.

However, do not treat:

```python
blit=True
```

as a magic fix.

If the animation is logically incorrect, changing `blit` will not repair the underlying logic.

---

# 14. Saving an Animation

Animations can be saved, for example:

```python
ani.save(
    'sine_wave_animation.mp4',
    writer='ffmpeg'
)
```

The original course material uses FFmpeg for MP4 output.

The important distinction is:

```text
plt.show()
```

means:

> display the animation

whereas:

```python
ani.save(...)
```

means:

> encode/save the animation to a file.

Depending on your environment, FFmpeg must be installed and available.

---

# 15. Debugging 3D Graphics

A graph can be syntactically correct and still be scientifically misleading.

## Check 1 — Data lengths

Before plotting:

```python
print(len(x), len(y), len(z))
```

For point-by-point plotting, confirm that the lengths agree.

## Check 2 — Inspect actual values

```python
print(x[:10])
print(y[:10])
print(z[:10])
```

This is often more useful than staring at a graph.

## Check 3 — Check ranges

```python
print(min(x), max(x))
print(min(y), max(y))
print(min(z), max(z))
```

A variable with a very different scale can make the visualization difficult to interpret.

## Check 4 — Check labels

Ask:

```text
What does X represent?
What does Y represent?
What does Z represent?
What are the units?
```

A beautiful graph with meaningless labels is not a good scientific visualization.

---

# 16. Debugging Animations Systematically

When an animation fails, use this checklist:

### Step 1 — Does the data exist?

```python
print(x[:5])
print(y[:5])
```

### Step 2 — Does the update function run?

```python
print("Animating frame:", frame)
```

### Step 3 — Does the frame have a sensible value?

```python
print(frame)
```

### Step 4 — Are the sliced arrays compatible?

```python
print(len(x[:frame]))
print(len(y[:frame]))
```

### Step 5 — Is the graphical object updated?

```python
line.set_data(...)
```

### Step 6 — Are the axis limits appropriate?

For example:

```python
ax.set_xlim(...)
ax.set_ylim(...)
```

### Step 7 — Only then investigate rendering/environment issues.

This is an example of **debugging by narrowing the problem**, rather than randomly changing code.

---

# 17. 3D Graphics on Google Colab

The original course material also demonstrates Plotly:

```python
import plotly.graph_objects as go

fig = go.Figure(
    data=[
        go.Scatter3d(
            x=x,
            y=y,
            z=z,
            mode="markers",
            marker=dict(
                size=5,
                color=z,
                colorscale="Viridis",
                opacity=0.8
            )
        )
    ]
)

fig.update_layout(
    scene=dict(
        xaxis_title="X Axis",
        yaxis_title="Y Axis",
        zaxis_title="Z Axis"
    )
)

fig.show()
```

This is useful because interactive 3D graphics can allow the viewer to rotate and inspect the data.

But notice the conceptual similarity:

```text
data
 ↓
x, y, z
 ↓
visual object
 ↓
labels/layout
 ↓
display
```

The library changes; the visualization reasoning does not.

---

# 18. Challenge — Scientific 3D Motion

Consider a moving particle:

\[
x(t)=\cos(t)
\]

\[
y(t)=\sin(t)
\]

\[
z(t)=t
\]

Write:

```python
t = np.linspace(0, 10, 200)

x = np.cos(t)
y = np.sin(t)
z = t
```

Create a 3D line plot.

### Predict

What shape should the particle trace?

Do not search for the answer first. Use the equations to reason about it.

### Extension

Create an animation in which the particle gradually traces the path.

Hint:

```python
line, = ax.plot([], [], [])
```

and then update all three coordinates.

---

# 19. Challenge — Modify Existing Code

Start with the sine-wave animation.

Modify it so that:

1. the amplitude can be changed;
2. the frequency can be changed;
3. the title displays the current frame;
4. the animation does not exceed the axis limits.

Do not rewrite the entire program.

Identify exactly which lines you changed and why.

---

# 20. Exit Questions

Before leaving this lecture, answer these without looking at the examples.

### Q1
What is the difference between a 2D point and a 3D point?

### Q2
Why must `x`, `y`, and `z` usually have matching lengths for a 3D scatter plot?

### Q3
What does:

```python
projection='3d'
```

do?

### Q4
What is the difference between `scatter()` and `plot()`?

### Q5
What is a frame in an animation?

### Q6
What is the purpose of `update(frame)`?

### Q7
Why is:

```python
x[:frame]
```

useful for animation?

### Q8
If `update()` is printing frame numbers but nothing appears, what should you investigate next?

### Q9
Why can a graph be technically correct but scientifically poor?

### Q10
What is one advantage of debugging the data before debugging the visualization library?

---

# Key Takeaways

The important lesson of this lecture is not memorizing:

```python
ax.scatter(...)
```

or:

```python
FuncAnimation(...)
```

The deeper model is:

```text
Scientific question
        ↓
Data
        ↓
Check the data
        ↓
Choose visualization
        ↓
Create graphical object
        ↓
Display / animate
        ↓
Inspect result
        ↓
Debug
        ↓
Interpret
```

For 3D visualization:

```text
(x, y, z)
```

represents a three-dimensional observation.

For animation:

```text
frame
   ↓
update(frame)
   ↓
new graphical state
```

represents change over time.

And for scientific programming:

> **A visualization is not the conclusion. It is a tool for helping us inspect and communicate the data.**
