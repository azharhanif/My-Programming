# Lecture 1: Intro to Programming

### **Table of Contents**

1. [Introduction to Programming](#introduction-to-programming)
2. [Statements and Expressions](#statements-and-expressions)
   - [What is a Statement?](#what-is-a-statement)
   - [What is an Expression?](#what-is-an-expression)
3. [Variables and Assignments](#variables-and-assignments)
   - [Naming Conventions](#naming-conventions)
4. [Working with Data Types](#working-with-data-types)
5. [Input and Output Statements](#input-and-output-statements)
6. [Fundamental Programming Principles](#fundamental-programming-principles)
   - [Naming Conventions](#naming-conventions-principles)
   - [Keep It Simple, Stupid (KISS)](#keep-it-simple-stupid-kiss)
   - [Open/Closed Principle](#open-closed-principle)
   - [Don't Repeat Yourself (DRY)](#dont-repeat-yourself-dry)
   - [Early Testing and Debugging](#early-testing-and-debugging)

### 1. **Introduction to Programming in Python**

A **programming language** like Python is a tool that allows humans to communicate instructions to a computer to solve problems. Programming involves writing code that follows a specific syntax and logic, which the computer can then interpret and execute. Python is a versatile and widely used programming language, particularly popular for scientific computing due to its ease of use and readability.

### 2. **Statements and Expressions**

#### **What is a Statement?**
In programming, a **statement** is a single line of code that performs an operation. In Python, statements can include assignments, function calls, loops, and conditionals.

Example:
```python
x = 10  # Assignment statement
print(x)  # Function call statement
```

Each statement executes an action, such as assigning a value to a variable or calling a function.

#### **What is an Expression?**
An **expression** is a combination of variables, values, and operators that evaluates to a result. In Python, expressions produce values that can be used in other statements.

Example:
```python
y = x + 5  # x + 5 is an expression that evaluates to 15 if x is 10
```

### 3. **Variables and Assignments**

A **variable** is a name associated with a value that can change during the execution of a program. **Assignment** is the process of giving a value to a variable.

Example:
```python
temperature = 25  # Assigning a value to a variable
```

#### **Naming Conventions**
In Python, good naming conventions are important for maintaining clear and readable code. Some best practices for naming variables and functions include:
- **Use descriptive names**: e.g., `temperature`, `distance`, `calculate_speed`.
- **Use snake_case** for variables and functions: e.g., `calculate_speed`.
- **Avoid reserved keywords**: such as `if`, `for`, `while`, etc.
- **Start with a letter**: Variables should start with a letter, not a number.

### 4. **Working with Data Types**

Python has several built-in data types, which are essential for working with different kinds of data. Some common types include:
- **int**: Integer numbers, e.g., `5`, `100`.
- **float**: Floating-point numbers, e.g., `3.14`, `-0.001`.
- **str**: String (text) data, e.g., `"Hello, world!"`.
- **bool**: Boolean values (`True` or `False`).
- **list**: A collection of items, e.g., `[1, 2, 3]`.
- **tuple**: An immutable collection of items, e.g., `(1, 2, 3)`.

Python also supports **dynamic typing**, meaning you don't need to specify the data type when declaring a variable.

Example:
```python
age = 30  # Integer
name = "Alice"  # String
height = 1.75  # Float
```

### 5. **Input and Output Statements**

**Input** allows the user to provide data to the program, while **output** displays results to the user.

#### **Input**
In Python, input can be taken using the `input()` function, which returns a string. You can then convert it to other data types as needed.

Example:
```python
name = input("Enter your name: ")  # Input
age = int(input("Enter your age: "))  # Input and conversion to int
```

#### **Output**
Output is displayed using the `print()` function.

Example:
```python
print("Hello, " + name)  # Output
print("Your age is " + str(age))  # Output (converted to string)
```

### 6. **Fundamental Programming Principles**

These principles help to write better, cleaner, and more maintainable code.

#### **Naming Conventions (Principles)**
Following consistent and meaningful naming conventions for variables and functions makes code easier to read and maintain. Use **descriptive names** and follow **snake_case** style in Python.

#### **Keep It Simple, Stupid (KISS)**
The KISS principle emphasizes that solutions should be simple. Avoid overcomplicating code. In Python, you can use built-in functions and libraries to simplify your tasks.

Key takeaway: **Write clear, simple, and easy-to-understand code.**

#### **Open/Closed Principle**
The Open/Closed Principle suggests that software entities (such as classes or functions) should be **open for extension**, but **closed for modification**. This is especially useful in object-oriented programming when building more flexible and reusable code.

Key takeaway: **Extend, don’t modify**.

#### **Don't Repeat Yourself (DRY)**
Avoid repeating code. If you find yourself writing similar code multiple times, refactor it into a reusable function or method. Python's functions and modules can help you implement this principle effectively.

Key takeaway: **Write reusable code and reduce redundancy.**

#### **Early Testing and Debugging**
Testing and debugging are essential in programming. Start testing your code early in the development process to ensure it works as expected. Python provides built-in tools like `assert` and the `unittest` module for automated testing.

Key takeaway: **Test early and often to catch errors quickly.**