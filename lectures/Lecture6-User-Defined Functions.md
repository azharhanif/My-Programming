# Lecture 6: User-Defined Functions

### **Table of Contents**

1. [Introduction to User-Defined Functions](#introduction-to-user-defined-functions)
2. [Naming Conventions for Functions](#naming-conventions-for-functions)
3. [Keep It Simple, Stupid (KISS) and Single Responsibility](#keep-it-simple-stupid-kiss-and-single-responsibility)
4. [Open/Closed Principle in Functions](#open-closed-principle-in-functions)
5. [Enhance Code Structure and Logic Through Functions](#enhance-code-structure-and-logic-through-functions)
6. [Refactoring Code](#refactoring-code)

### 1. **Introduction to User-Defined Functions**

A **user-defined function** in Python is a block of reusable code that performs a specific task. Functions help break down complex problems into smaller, manageable pieces and improve code reusability. Functions make code more modular, allowing you to call them multiple times with different inputs.

#### Syntax:
```python
def function_name(parameters):
    # Code block to execute
    return result
```

- **`def`**: Keyword used to define a function.
- **`function_name`**: Name of the function (following Python's naming conventions).
- **`parameters`**: Input values passed to the function (optional).
- **`return`**: Returns a value from the function (optional).

Example:
```python
def greet(name):
    return "Hello, " + name + "!"
    
print(greet("Alice"))
```

This will output:
```
Hello, Alice!
```

### 2. **Naming Conventions for Functions**

Naming conventions are important for writing clean, readable code. By following consistent naming conventions, you help other developers (and yourself) understand what each function does. Here are some common conventions for Python functions:

- **Use descriptive names**: The function name should clearly describe what the function does. For example, use `calculate_area()` instead of `calc()`.
- **Use snake_case**: In Python, function names should be written in **snake_case**, meaning all letters are lowercase, and words are separated by underscores. For example, `calculate_speed()` is preferred over `CalculateSpeed()`.
- **Avoid overly generic names**: Avoid using names like `do_stuff()` or `function1()` that don't describe the function's behavior.

Good example:
```python
def calculate_area(radius):
    return 3.14 * radius ** 2
```

### 3. **Keep It Simple, Stupid (KISS) and Single Responsibility**

The **KISS principle** suggests that functions should be simple and easy to understand. Overcomplicating a function can lead to bugs and maintenance challenges. Functions should do one thing and do it well.

#### **Single Responsibility**:
Each function should have a **single responsibility**, meaning it should only perform one specific task. A function that tries to do too many things can become difficult to understand and debug.

Example:
- **Bad**: A function that calculates the area and prints a message.
```python
def area_and_message(radius):
    area = 3.14 * radius ** 2
    print("The area is:", area)
    return area
```

- **Good**: Two separate functions, each with a single responsibility.
```python
def calculate_area(radius):
    return 3.14 * radius ** 2

def print_area(area):
    print("The area is:", area)
```

### 4. **Open/Closed Principle in Functions**

The **Open/Closed Principle** suggests that software entities (like functions) should be **open for extension**, but **closed for modification**. This means you should be able to add new functionality to a function without changing its original code.

In Python, you can achieve this principle by writing functions that can easily be extended with new functionality.

Example:
```python
# Original function that calculates area of a circle
def calculate_area(radius):
    return 3.14 * radius ** 2

# Extended function that also calculates the circumference without modifying the original function
def calculate_circumference(radius):
    return 2 * 3.14 * radius
```

Here, you’ve extended the functionality by adding `calculate_circumference()` without modifying the original `calculate_area()` function, which adheres to the Open/Closed Principle.

### 5. **Enhance Code Structure and Logic Through Functions**

One of the key benefits of functions is that they allow you to structure your code more logically. You can break down large problems into smaller, more manageable tasks by using functions to represent different parts of your logic.

For example, if you are solving a physics problem involving the calculation of velocity, distance, and time, you could break the problem down into separate functions:
```python
def calculate_velocity(distance, time):
    return distance / time

def calculate_distance(velocity, time):
    return velocity * time

def calculate_time(distance, velocity):
    return distance / velocity
```

Now, instead of writing a long and complex series of calculations, you can reuse these smaller functions throughout your code to keep everything organized.

### 6. **Refactoring Code**

**Refactoring** refers to the process of restructuring existing code without changing its external behavior. It improves the readability, maintainability, and efficiency of code. You might refactor code to eliminate duplication, improve naming conventions, or simplify complex logic.

Common reasons to refactor code:
- **Simplify complex functions**: If a function is doing too much, break it into smaller, more manageable pieces.
- **Improve readability**: Make the code more understandable to other developers (or your future self).
- **Eliminate redundant code**: If the same logic is repeated, refactor it into a function or loop.

Example of refactoring:
```python
# Original code
def total_cost(price1, price2, price3):
    return price1 + price2 + price3

# Refactored code with a loop
def total_cost(prices):
    total = 0
    for price in prices:
        total += price
    return total
```

The refactored version is more scalable because it can handle any number of prices without modifying the function.

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

# Lecture 6: User-Defined Functions — Designing Reusable Solutions

## 0. Why functions?

A long program can become difficult to reason about if everything happens in one block.

A function gives a problem a name:

```python
calculate_velocity(distance, time)
```

Now the program communicates its intent.

## 1. Function Anatomy

```python
def calculate_velocity(distance, time):
    return distance / time
```

- `def` defines the function.
- `distance` and `time` are parameters.
- `return` sends a result to the caller.

Calling:

```python
v = calculate_velocity(100, 20)
```

passes `100` and `20` as arguments.

## 2. Trace a Function Call

```python
def double(x):
    return x * 2

a = 5
b = double(a)
```

Trace:

```text
a = 5
double(5)
x = 5
return 10
b = 10
```

The parameter `x` is local to the function.

## 3. `return` vs `print`

Compare:

```python
def square(x):
    print(x * x)
```

with:

```python
def square(x):
    return x * x
```

The second is more reusable:

```python
answer = square(5)
print(answer + 10)
```

A function that returns a value can be composed with other operations.

## 4. Single Responsibility

Weak:

```python
def analyze_temperature():
    # read input
    # validate input
    # calculate average
    # print report
    # write file
```

Better separation:

```python
def read_temperature():
    ...

def calculate_average(values):
    ...

def print_report(average):
    ...
```

Each function has a clearer responsibility.

## 5. Refactoring

Original:

```python
distance = 100
time = 20
velocity = distance / time
print(velocity)

distance = 50
time = 10
velocity = distance / time
print(velocity)
```

Refactor:

```python
def calculate_velocity(distance, time):
    return distance / time

print(calculate_velocity(100, 20))
print(calculate_velocity(50, 10))
```

The behavior is preserved while repetition is reduced.

## 6. Function Contracts

For each function, be able to state:

```text
Input:
Output:
Assumptions:
Possible invalid input:
```

Example:

```python
def calculate_velocity(distance, time):
    return distance / time
```

Contract:

```text
Input: numeric distance and time
Output: velocity
Assumption: time != 0
```

This makes debugging much easier.

## 7. Open/Closed Principle — Use Carefully

The original course introduces Open/Closed. The important beginner interpretation is:

> Prefer adding a new function for a genuinely new operation rather than repeatedly making one function more complicated.

Avoid turning one function into:

```python
if operation == "area":
...
elif operation == "volume":
...
elif operation == "speed":
...
elif operation == "temperature":
...
```

unless that design is actually appropriate.

## 8. Active-Learning Questions

1. What is the difference between a parameter and an argument?
2. Why is `return` usually more reusable than `print`?
3. What should a function's name communicate?
4. When should a large function be split?
5. What assumptions belong in a function contract?

## 9. Challenge

Create:

```python
def calculate_kinetic_energy(mass, velocity):
    ...
```

Then create:

```python
def calculate_momentum(mass, velocity):
    ...
```

Finally write a short main program that calls both functions.

Do not duplicate the formulas or mix input/output responsibilities into the calculation functions.
