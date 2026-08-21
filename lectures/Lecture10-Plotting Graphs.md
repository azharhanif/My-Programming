# Lecture 10: Plotting Graphs — From Data to Visual Evidence

## 0. Why plotting belongs in programming

A graph is not decoration.

A useful scientific graph can reveal:

- trends;
- outliers;
- relationships;
- unexpected measurements;
- model disagreement.

The workflow is:

```text
data → check → plot → interpret
```

## 1. Matplotlib

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.plot(x, y)
plt.show()
```

Before running it, predict the shape of the graph.

## 2. Labels Are Part of Correctness

```python
plt.plot(x, y)
plt.title("Distance vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Distance (m)")
plt.show()
```

A graph without units can be scientifically ambiguous.

## 3. Plot the Model vs Measurements

Suppose:

```python
time = [0, 1, 2, 3, 4]
measured = [0.0, 4.9, 19.7, 44.2, 78.5]
model = [0.0, 4.9, 19.6, 44.1, 78.4]
```

Plot both:

```python
plt.plot(time, measured, label="Measured")
plt.plot(time, model, label="Model")

plt.xlabel("Time (s)")
plt.ylabel("Distance (m)")
plt.title("Measured vs Model")
plt.legend()
plt.show()
```

The important question is not merely:

> "Can I make the graph?"

It is:

> "What does the graph tell me?"

## 4. Data Shape Check

Before plotting:

```python
print(len(time))
print(len(measured))
```

The x and y collections must have compatible lengths.

## 5. Plotting From a File

Typical pipeline:

```text
CSV
 ↓
read
 ↓
convert numeric values
 ↓
store lists
 ↓
plot
 ↓
interpret
```

Do not plot raw strings.

## 6. Density Plots

The original course introduces Seaborn/KDE plots.

Conceptually, a density plot estimates how data are distributed.

```python
import seaborn as sns
import matplotlib.pyplot as plt

sns.kdeplot(data)
plt.show()
```

Before using it, ask:

- Is the data numeric?
- Is the sample size reasonable?
- What does the distribution represent?
- Is a histogram perhaps more appropriate?

## 7. A Scientific Warning

A smooth graph can make noisy data look convincing.

Visualization does not prove a hypothesis.

Always separate:

```text
What the graph shows
```

from:

```text
What you conclude from it
```

## 8. Debugging Plot Code

If nothing appears:

- confirm the plotting library is imported;
- confirm the code reaches `plt.show()`;
- inspect the data;
- check lengths;
- check numeric types.

If the graph looks wrong:

- inspect x and y values;
- check units;
- check whether the values were converted correctly;
- compare a few points manually.

## 9. Active-Learning Questions

1. Why should axes have units?
2. Why should measured and modeled data often be plotted together?
3. What can a graph reveal that a table may hide?
4. Why can a visually smooth graph still be misleading?
5. What would you inspect first if the graph has the wrong shape?

## 10. Challenge

Read a small CSV dataset containing:

```text
time,measured_temperature
```

Then:

1. plot measured temperature against time;
2. label both axes with units;
3. add a title;
4. calculate and display the maximum temperature;
5. identify the time at which it occurs;
6. write two sentences interpreting the graph.

The final two sentences are part of the programming task: **data visualization is useful only when the programmer can interpret the result.**
