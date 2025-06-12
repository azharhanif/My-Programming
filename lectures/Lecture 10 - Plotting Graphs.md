# Lecture 10: Plotting Graphs

### **Table of Contents**

1. [Introduction to Plotting in Python](#introduction-to-plotting-in-python)
2. [Plotting Simple Graphs Using `plot()` and `show()`](#plotting-simple-graphs-using-plot-and-show)
3. [Creating Density Plots](#creating-density-plots)
4. [Debugging and Testing Plotting Operations](#debugging-and-testing-plotting-operations)

### 1. **Introduction to Plotting in Python**

Plotting data is a critical aspect of data analysis and visualization. Python provides several libraries for plotting graphs, and the most popular one is **Matplotlib**. The **matplotlib.pyplot** module provides a set of functions for creating various types of graphs, such as line plots, scatter plots, bar charts, and more.

In this lecture, we will focus on two important aspects of plotting:
- **Simple line plots** using `plot()` and `show()`.
- **Density plots**, which visualize the distribution of data.

To get started with plotting, you first need to install and import **Matplotlib**. If you don’t have it installed, you can install it using the following command:
```bash
pip install matplotlib
```

Then, import **Matplotlib** in your code:
```python
import matplotlib.pyplot as plt
```

### 2. **Plotting Simple Graphs Using `plot()` and `show()`**

The **plot()** function is used to create line plots in Matplotlib. You can use this function to plot data points on a graph, and the **show()** function is used to display the plot.

#### Basic Syntax of `plot()`:
```python
plt.plot(x, y)  # x and y are lists or arrays of data points
```

#### `show()` Function:
After creating the plot with `plot()`, use `plt.show()` to display the graph.

#### Example: Plotting a Simple Line Graph
```python
import matplotlib.pyplot as plt

# Data for the plot
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Create a line plot
plt.plot(x, y)

# Display the plot
plt.show()
```

This code will create a simple line plot with `x` values on the x-axis and `y` values on the y-axis.

#### Adding Labels and Title:
You can customize your plot by adding a title and labels for the axes.

Example:
```python
plt.plot(x, y)
plt.title('Simple Line Plot')  # Adding a title
plt.xlabel('X Values')  # Adding a label for the x-axis
plt.ylabel('Y Values')  # Adding a label for the y-axis
plt.show()
```

### 3. **Creating Density Plots**

A **Density Plot** is a smooth representation of the distribution of a dataset. It provides a more continuous representation of the data's distribution compared to histograms. In Matplotlib, you can use **Seaborn**, another library built on top of Matplotlib, to create density plots. Seaborn provides a more convenient interface for complex plotting.

If you don't have Seaborn installed, you can install it with:
```bash
pip install seaborn
```

#### Basic Syntax for Density Plot:
```python
import seaborn as sns
sns.kdeplot(data)
```

Here, **`kdeplot`** stands for Kernel Density Estimation Plot, which is used to visualize the data distribution.

#### Example: Creating a Density Plot
```python
import seaborn as sns
import matplotlib.pyplot as plt

# Sample data: Normally distributed data
import numpy as np
data = np.random.normal(size=1000)

# Create the density plot
sns.kdeplot(data)

# Display the plot
plt.show()
```

In this example, `data` is a sample of 1000 random values drawn from a normal distribution. The **`kdeplot()`** function generates the density plot, which will show the smooth distribution of the data.

#### Customizing the Density Plot:
You can customize the appearance of the density plot by changing its color, style, and bandwidth (which controls the smoothness of the plot).

Example with customizations:
```python
sns.kdeplot(data, color='green', shade=True, bw_adjust=0.5)  # Adjust the bandwidth for smoothness
plt.show()
```

- **`color`**: Sets the color of the plot.
- **`shade`**: Fills the area under the curve with color.
- **`bw_adjust`**: Adjusts the bandwidth, which controls the smoothness of the density plot.

### 4. **Debugging and Testing Plotting Operations**

When working with plots, it's essential to ensure that your data is correctly formatted and that your plotting functions are used properly. Here are some debugging tips:

#### Checking Data:
Ensure your data is in the correct format (e.g., lists or arrays) and contains no missing or invalid values.
```python
# Check the type and shape of your data
print(type(x), len(x))  # Ensure x is a list or array and has the correct length
```

#### Handling Errors in Plotting:
- **Empty data**: Make sure that your data is not empty.
- **Mismatched dimensions**: Ensure that the x and y data points have the same length when plotting.

Example of checking for empty data:
```python
if len(x) == 0 or len(y) == 0:
    print("Error: Data is empty")
else:
    plt.plot(x, y)
    plt.show()
```

#### Testing Plot Appearance:
- **Labels and title**: Ensure that your labels and titles are correctly placed and readable.
- **Adjusting figure size**: If the plot appears too small or too large, you can adjust the figure size using:
```python
plt.figure(figsize=(8, 6))  # Adjust the figure size (width, height)
```

Example with figure size adjustment:
```python
plt.figure(figsize=(10, 6))
plt.plot(x, y)
plt.title('Custom Plot with Adjusted Size')
plt.show()
```

#### Testing Density Plot:
- Make sure the data you're passing to the **`kdeplot()`** function is numeric and has a reasonable distribution.
- You can use `np.random.normal()` or `np.random.uniform()` to create sample datasets for testing.

Example:
```python
import numpy as np
data = np.random.normal(size=500)
sns.kdeplot(data)
plt.show()
```