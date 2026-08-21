# Lecture 7: Lists and Arrays


### **Table of Contents**

1. [Introduction to Lists and Single Dimensional Arrays](#introduction-to-lists-and-single-dimensional-arrays)
2. [Don't Repeat Yourself (DRY) Principle](#dont-repeat-yourself-dry-principle)
3. [Arithmetic Operations with Arrays](#arithmetic-operations-with-arrays)
4. [Debugging and Testing Array Operations](#debugging-and-testing-array-operations)

### 1. **Introduction to Lists and Single Dimensional Arrays**

In Python, the most common way to represent a collection of items is by using **lists**. A **list** is a data structure that can hold multiple items, such as numbers, strings, or other lists. Lists are **ordered**, **mutable**, and **allow duplicate values**.

While **Python lists** are not strictly the same as arrays in other programming languages (like C++ or Java), they are similar in that they allow you to store a collection of elements and access them using indices.

A **single-dimensional array** is essentially a list where all elements are arranged in a single line or sequence.

#### Basic List Syntax:
```python
my_list = [10, 20, 30, 40, 50]  # A list of integers
```

#### Accessing Elements in a List:
You can access elements in a list using **indexing**:
```python
first_element = my_list[0]  # Accesses the first element, 10
last_element = my_list[-1]  # Accesses the last element, 50
```

You can also use **slicing** to access a subset of a list:
```python
subset = my_list[1:4]  # Accesses elements from index 1 to 3, i.e., [20, 30, 40]
```

### 2. **Don't Repeat Yourself (DRY) Principle**

The **Don't Repeat Yourself (DRY)** principle emphasizes reducing repetition in code. When the same logic is repeated multiple times, it increases the chances of errors and makes the code harder to maintain. Instead of repeating the same code, you can use **functions** or **loops** to handle repetitive tasks.

#### DRY in Lists:
In Python, using loops and functions can help avoid repetition. For example, instead of manually summing elements of a list multiple times, you can create a function that performs this operation.

Example:
```python
# Repetitive code without DRY
sum1 = 10 + 20 + 30
sum2 = 40 + 50 + 60

# DRY approach using a function
def calculate_sum(numbers):
    return sum(numbers)

numbers1 = [10, 20, 30]
numbers2 = [40, 50, 60]
print(calculate_sum(numbers1))  # Output: 60
print(calculate_sum(numbers2))  # Output: 150
```

By using the DRY principle, the calculation logic is now reusable and easier to maintain.

### 3. **Arithmetic Operations with Arrays**

Arrays (or lists) allow you to perform arithmetic operations on their elements. You can use Python’s built-in operators, or you can use the **NumPy** library for more advanced array operations. However, we will start with basic arithmetic operations using lists without external libraries.

#### Basic Arithmetic Operations on Lists:
You can perform arithmetic operations like addition, subtraction, multiplication, and division on the elements of a list using a **for loop** or **list comprehension**.

Example of addition (adding the same number to each element of the list):
```python
numbers = [10, 20, 30, 40]

# Adding 5 to each element
new_numbers = [num + 5 for num in numbers]
print(new_numbers)  # Output: [15, 25, 35, 45]
```

#### Example of multiplication (multiplying each element by 2):
```python
numbers = [1, 2, 3, 4]

# Multiplying each element by 2
multiplied_numbers = [num * 2 for num in numbers]
print(multiplied_numbers)  # Output: [2, 4, 6, 8]
```

#### Summing All Elements:
To calculate the sum of all elements in a list, you can use Python’s built-in `sum()` function:
```python
numbers = [10, 20, 30, 40]
total = sum(numbers)
print(total)  # Output: 100
```

#### Performing Element-wise Arithmetic Operations:
You can perform element-wise operations on two lists using a **for loop** or **list comprehension**. For example, if you want to add corresponding elements of two lists:

```python
list1 = [10, 20, 30]
list2 = [1, 2, 3]

# Adding corresponding elements
sum_lists = [a + b for a, b in zip(list1, list2)]
print(sum_lists)  # Output: [11, 22, 33]
```

The `zip()` function pairs up corresponding elements from two lists, allowing you to perform the operation on them in parallel.

### 4. **Debugging and Testing Array Operations**

When working with lists and arrays, it's important to ensure that the operations are being performed correctly. Here are some debugging techniques for working with arrays:

#### Print Statements
Use **print statements** to check the values of the array before and after operations:
```python
numbers = [10, 20, 30]

# Debugging: Check the array before performing arithmetic
print("Original numbers:", numbers)

# Perform an operation
updated_numbers = [num + 5 for num in numbers]

# Debugging: Check the updated array
print("Updated numbers:", updated_numbers)
```

#### Testing Edge Cases
Test the behavior of the array operations with edge cases:
- **Empty lists**: Check if your code handles empty arrays gracefully.
- **Large numbers**: Ensure the operations work correctly with large numbers.
- **Negative numbers**: Check how your code handles negative values.

Example with an empty list:
```python
numbers = []

# Avoid errors when performing operations on an empty list
if numbers:
    updated_numbers = [num + 5 for num in numbers]
    print("Updated numbers:", updated_numbers)
else:
    print("The list is empty!")

```

## Multiple user inputs into a list in Python
#### Using input() and split()
One of the simplest ways to take multiple inputs from a user in Python is by using the input() function along with the split() method. The split() method splits a string into a list based on a specified separator (by default, it uses whitespace).

Example:
```java
# taking two inputs at a time
x, y, z = input("Values: ").split()
print(x)
print(y)
print(z)
```
#### How it Works:
input() takes the full input as a single string.

.split() divides the string into separate components based on whitespace by default.

The values are assigned to individual variables (x, y, z).

#### Taking Multiple Inputs in a Loop
If you want to collect multiple inputs from the user one at a time, you can use a loop. This is particularly useful when you need to collect an arbitrary number of inputs or perform validation on each input.
```java
# Create an empty list to store the inputs
a = []

# Ask the user for how many items they want to input
b = int(input("How many items do you want to enter? "))

# Loop to collect multiple inputs
for i in range(b):
    val = input(f"Enter item {i + 1}: ")
    a.append(val)


for i in a:
    print(i)
```
#### Explanation:

We first ask how many items the user wants to input.

We then use a loop to take inputs one by one, appending each input to a list.

After the loop finishes, we print the collected items.

This approach gives the user the flexibility to enter as many items as needed.

---


## New-Semester Learning Cycle

For each major example, use this sequence:

1. **Read the problem**
2. **Predict** what the code should do
3. **Trace** the important variables
4. **Code** the smallest working version
5. **Run and inspect**
6. **Debug** one problem at a time
7. **Modify** the solution
8. **Explain the design choice**

The goal is not to make the course easier. The goal is to make the reasoning visible so that a student who is still developing programming fluency can follow the path from a scientific problem to a correct Python solution.


---

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
