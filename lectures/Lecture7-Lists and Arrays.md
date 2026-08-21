# Lecture 7: Lists and Arrays — Working With Collections

## 0. From one value to many

A scientific program rarely processes only one measurement.

Instead of:

```python
temperature1 = 20
temperature2 = 22
temperature3 = 21
```

use:

```python
temperatures = [20, 22, 21]
```

This makes repetition and analysis possible.

## 1. Indexing

```python
values = [10, 20, 30, 40]

values[0]  # 10
values[-1] # 40
```

Indexes start at zero.

## 2. Slicing

```python
values[1:3]
```

produces:

```text
[20, 30]
```

The stop index is excluded.

A useful mental model:

```text
start included
stop excluded
```

## 3. Mutation

Lists are mutable:

```python
values[1] = 99
```

Now the original list has changed.

This is different from creating a new list:

```python
new_values = [x + 5 for x in values]
```

## 4. Trace a List Algorithm

```python
values = [3, 8, 2]

total = 0

for value in values:
    total += value

print(total)
```

Trace the accumulator before and after every iteration.

## 5. Built-in Functions vs Algorithms

```python
sum(values)
max(values)
min(values)
len(values)
```

are useful.

But understanding the loop behind:

```python
sum(values)
```

is still important because it teaches the accumulation pattern.

## 6. Element-wise Operations

```python
values = [10, 20, 30]

result = [value * 2 for value in values]
```

produces:

```text
[20, 40, 60]
```

This is a list comprehension.

Use it when the transformation is simple and readable.

## 7. Two-List Operations

```python
a = [10, 20, 30]
b = [1, 2, 3]

result = [x + y for x, y in zip(a, b)]
```

Before using `zip`, ask:

> Are these lists supposed to have corresponding elements?

If lengths differ, the result follows the shorter input.

## 8. Multiple User Inputs

```python
x, y, z = input("Values: ").split()
```

Remember: the values are strings.

For numeric data:

```python
x, y, z = map(float, input("Values: ").split())
```

This is a useful place to slow down and explain type conversion.

## 9. Active-Learning Questions

1. Why does `values[-1]` access the final element?
2. Why is `values[1:3]` two elements rather than three?
3. What happens to the original list when an element is assigned?
4. When is a list comprehension clearer than a loop?
5. Why does `zip()` make sense for element-wise operations?

## 10. Scientific Challenge

Given:

```python
measurements = [12.4, 13.1, 11.8, 14.0, 12.7]
```

calculate:

- mean;
- minimum;
- maximum;
- range (`max - min`);
- a new list containing each measurement minus the mean.

First write the algorithm in plain language. Then code it.

## 11. Design Question

A student writes five nearly identical loops for five lists.

Ask:

> Is this a data problem, a loop problem, or a function-design problem?

The best answer often involves combining a function with iteration.
