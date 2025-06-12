# Lecture 5: Iterative Logic

### **Table of Contents**

1. [Introduction to Iterative Logic](#introduction-to-iterative-logic)
2. [The For Loop](#the-for-loop)
3. [The While Loop](#the-while-loop)
4. [Break and Continue Statements](#break-and-continue-statements)
5. [Debugging and Testing Iterative Logic](#debugging-and-testing-iterative-logic)

### 1. **Introduction to Iterative Logic**

**Iterative logic** is used in programming when you need to repeat certain tasks or operations multiple times. This repetition is done through **loops**, which allow you to execute a block of code as long as a specific condition is true.

There are two main types of loops in Python:
- The **For loop**: Used when you know in advance how many times you want to repeat a block of code.
- The **While loop**: Used when you want to repeat a block of code as long as a condition is true, but you may not know how many iterations will be needed.

Both loops allow you to perform repetitive tasks efficiently, and they can be controlled further with **Break** and **Continue** statements.

### 2. **The For Loop**

The **For loop** is used to iterate over a sequence (such as a list, tuple, or string) or a range of numbers. It automatically keeps track of the number of iterations, making it ideal when you know how many times you need to repeat a task.

#### Syntax:
```python
for variable in sequence:
    # Code to execute for each item in the sequence
```

The **variable** takes the value of each item in the **sequence** for each iteration.

Example:
```python
# Iterating through a list of numbers
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)
```

This will print:
```
1
2
3
4
5
```

The **range()** function is commonly used with **For loops** to generate a sequence of numbers:
```python
for i in range(5):  # Will iterate over numbers 0 to 4
    print(i)
```

This will print:
```
0
1
2
3
4
```

### 3. **The While Loop**

The **While loop** is used when you want to repeat a block of code as long as a certain condition is **true**. It is useful when you do not know in advance how many times the loop should run.

#### Syntax:
```python
while condition:
    # Code to execute as long as the condition is true
```

The loop continues to run until the **condition** becomes **false**.

Example:
```python
# Print numbers from 1 to 5 using a while loop
count = 1
while count <= 5:
    print(count)
    count += 1  # Increment the counter to avoid infinite loop
```

This will print:
```
1
2
3
4
5
```

### 4. **Break and Continue Statements**

**Break** and **Continue** are special statements used to control the flow of loops.

#### The **Break** Statement

The **break** statement is used to exit the loop prematurely, even if the loop condition is still true. It is often used when you want to stop the loop based on a specific condition.

Example:
```python
for i in range(10):
    if i == 5:
        break  # Exit the loop when i is equal to 5
    print(i)
```

This will print:
```
0
1
2
3
4
```
The loop stops when `i` reaches 5, and the remaining numbers are not printed.

#### The **Continue** Statement

The **continue** statement skips the current iteration of the loop and moves to the next iteration. It is used when you want to skip certain steps within the loop without exiting the entire loop.

Example:
```python
for i in range(10):
    if i == 5:
        continue  # Skip this iteration when i is equal to 5
    print(i)
```

This will print:
```
0
1
2
3
4
6
7
8
9
```

The number `5` is skipped because the loop continues to the next iteration when `i` is 5.

### 5. **Debugging and Testing Iterative Logic**

When working with loops, it’s essential to test and debug to avoid issues like **infinite loops** (when the loop never ends) or **off-by-one errors** (when the loop doesn’t iterate the expected number of times).

#### Debugging with Print Statements
- Use **print statements** to check if the loop is running as expected, especially to track variable values.
- Ensure that the loop condition is changing as intended to avoid infinite loops.

Example:
```python
count = 1
while count <= 5:
    print("Current count:", count)  # Debugging: Check the value of count
    count += 1
```

#### Testing Loops for Edge Cases
- Test loops with different ranges or boundary conditions to ensure they handle all situations, such as empty lists or starting from different values.

Example of testing a **For loop** with an empty list:
```python
numbers = []
for number in numbers:
    print(number)  # This will not print anything because the list is empty
```

Example of testing a **While loop** with boundary conditions:
```python
count = 0
while count < 5:
    print(count)
    count += 1
```

By using debugging techniques, such as checking variable values and testing edge cases, you can ensure that your loops behave as expected and perform the correct number of iterations.
