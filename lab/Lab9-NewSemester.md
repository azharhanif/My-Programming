# Programming in Science — Lab 9
## Scientific Visualization: From Data to Evidence

**Estimated time:** 80–100 minutes

### Learning objectives
You will practice:
- plotting paired data;
- labeling graphs scientifically;
- checking data before plotting;
- interpreting a graph rather than merely generating it;
- choosing an appropriate visualization;
- debugging plots.

---

# Part A — Curve plotting

Write:

```python
def plot_curve(x_values, y_values):
    ...
```

Plot the values using `plt.plot()`.

Include:

- title;
- x-axis label;
- y-axis label;
- `plt.show()`.

Before plotting, check:

```text
data is not empty
len(x_values) == len(y_values)
```

### Prediction

For:

```python
x = [1,2,3,4,5]
y = [1,4,9,16,25]
```

what shape do you expect?

Why?

---

# Part B — Hertzsprung–Russell diagram

Write:

```python
def plot_hr_diagram(temperature, luminosity):
    ...
```

Use a scatter plot.

Important scientific convention:

**Temperature should decrease from left to right.**

Label both axes and add a meaningful title.

### Explain

Why is a scatter plot appropriate here instead of a line connecting stars?

---

# Part C — Distribution visualization

Create at least 30 measurement values.

Plot a histogram or density-style visualization.

Print the first 10 values before plotting.

Explain in one or two sentences what the visualization tells us that a raw list does not.

---

# Part D — Debugging

Consider:

```python
x = [1, 2, 3, 4]
y = [1, 4, 9]

plt.plot(x, y)
```

What is wrong?

Why should the plotting function check lengths before calling `plot()`?

---

# Part E — Challenge

Create a function:

```python
def summarize_and_plot(x, y):
    ...
```

It should:

1. validate the data;
2. print the number of observations;
3. print the minimum and maximum y-values;
4. create a labeled plot.

Do not duplicate plotting logic elsewhere.

---

# Part F — Interpretation

For one graph you created, write:

1. What does the x-axis represent?
2. What does the y-axis represent?
3. What pattern do you see?
4. Is there an unusual value?
5. What scientific conclusion can you reasonably make?
6. What conclusion can you **not** make from the graph alone?
