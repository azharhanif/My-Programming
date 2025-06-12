# Lecture 11: 3D Graphs and Animations

### **Table of Contents**

1. [Introduction to 3D Graphics](#introduction-to-3d-graphics)
2. [Creating 3D Plots with Matplotlib](#creating-3d-plots-with-matplotlib)
3. [Creating Animations with Matplotlib](#creating-animations-with-matplotlib)
4. [Debugging and Testing 3D Graphics and Animations](#debugging-and-testing-3d-graphics-and-animations)

### 1. **Introduction to 3D Graphics**

**3D graphics** involve representing data in three dimensions (X, Y, and Z axes), allowing for a more complex and realistic visualization of data. 3D plots are particularly useful for visualizing data that has more than two variables, such as scientific simulations, physical systems, or geographic data.

In Python, we can use the **Matplotlib** library to create 3D graphics. The `mpl_toolkits.mplot3d` module is a part of Matplotlib that provides functions for creating 3D plots.

### 2. **Creating 3D Plots with Matplotlib**

To create 3D plots, you need to import the `Axes3D` module from `mpl_toolkits.mplot3d`. You can then define 3D axes using the `Axes3D` class.

#### Basic Syntax for Creating a 3D Plot:
```python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a figure
fig = plt.figure()

# Add 3D axes to the figure
ax = fig.add_subplot(111, projection='3d')

# Plot data points (example)
ax.scatter(x, y, z)  # Where x, y, z are lists or arrays of data points

# Display the plot
plt.show()
```

#### Example: Plotting a 3D Scatter Plot
```python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Data points
x = np.random.rand(100)
y = np.random.rand(100)
z = np.random.rand(100)

# Create a figure
fig = plt.figure()

# Add 3D axes to the figure
ax = fig.add_subplot(111, projection='3d')

# Plot data points
ax.scatter(x, y, z)

# Set labels for the axes
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')

# Show the plot
plt.show()
```

This creates a 3D scatter plot where the data points are randomly distributed along the X, Y, and Z axes.

#### Example: Plotting a 3D Scatter Plot on Google.Colab

```python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import plotly.graph_objects as go

# Data points
x = np.random.rand(100)
y = np.random.rand(100)
z = np.random.rand(100)

# Create a figure
fig = go.Figure(data=[go.Scatter3d(
    x=x, y=y, z=z,
    mode="markers",
    marker=dict(
        size=5,
        color=z,
        colorscale="Viridis",
        opacity=0.8
    )
)])

fig.update_layout(
    scene=dict(
        xaxis_title="X Axis",
        yaxis_title="Y Axis",
        zaxis_title="Z Axis",
    ),
    margin=dict(l=0, r=0, b=0, t=0)
)

fig.show()
```

#### 3D Line Plot:
You can also plot 3D lines using the `plot()` function in 3D space.

Example:
```python
# Define data for 3D line plot
x = np.linspace(0, 10, 100)
y = np.sin(x)
z = np.cos(x)

# Create figure and 3D axes
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the 3D line
ax.plot(x, y, z)

# Show the plot
plt.show()
```

### 3. **Creating Animations with Matplotlib**

**Animations** allow you to display changing data over time, making your visualizations more dynamic and engaging. In Python, **Matplotlib** provides the `FuncAnimation` class from the `matplotlib.animation` module to create animations.

#### Basic Syntax for Animations:
```python
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create a figure and axis
fig, ax = plt.subplots()

# Define the function to update the plot for each frame
def update(frame):
    # Update plot data here
    ax.clear()
    ax.plot(data[:frame])  # Example of updating plot with new data

# Create an animation
ani = FuncAnimation(fig, update, frames=range(1, len(data)), repeat=False)

# Display the animation
plt.show()
```

#### Example: Simple Line Animation
Here’s a basic example that animates a sine wave:

```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Generate data
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

# Create figure and axis
fig, ax = plt.subplots()

# Line that will be animated
line, = ax.plot([], [], lw=2)

# Set the limits of the plot
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-1, 1)

# Initialize function: this will be called to setup the background
def init():
    line.set_data([], [])
    return line,

# Update function: this will be called at each frame
def update(frame):
    line.set_data(x[:frame], y[:frame])
    return line,

# Create animation
ani = FuncAnimation(fig, update, frames=len(x), init_func=init, blit=True)

# Display the animation
plt.show()
```

This code animates a sine wave, showing the graph's development frame by frame.

#### Saving Animations:
You can save animations to a file (e.g., as an MP4 or GIF) using the `save()` method.

Example:
```python
ani.save('sine_wave_animation.mp4', writer='ffmpeg')
```

Make sure to have **FFmpeg** installed for saving as MP4 or other formats.

### 4. **Debugging and Testing 3D Graphics and Animations**

When working with **3D graphics** and **animations**, debugging is crucial to ensure that your visualizations are accurate and render correctly.

#### Debugging 3D Graphics:
- **Check the data**: Ensure that the data being plotted in 3D space is correctly structured, especially for large datasets. If points are not visible, check their ranges along the X, Y, and Z axes.
- **Check axis labels and limits**: Ensure that the axis labels are clear and the axes are properly scaled to fit the data.

Example:
```python
print(x[:10], y[:10], z[:10])  # Debugging: Check the first few points of the data
```

#### Debugging Animations:
- **Check the update function**: Ensure that the `update()` function is correctly updating the data in each frame. If the plot is not updating as expected, verify that the data is being modified correctly for each frame.
- **Check performance**: For complex animations, performance may be a concern. Ensure that the animation is smooth and that the `blit=True` option is used to optimize redrawing only the elements that change.

Example:
```python
print("Animating frame:", frame)  # Debugging: Print frame number to check animation progression
```

#### Handling Errors:
- If you encounter errors such as the plot not showing or the animation not working, check that Matplotlib is correctly installed, and the plot window is not being blocked by other processes or code.
