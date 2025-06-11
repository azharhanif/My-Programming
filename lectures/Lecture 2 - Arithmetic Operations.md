# Lecture 2: Arithmetic Operations

### **Table of Contents**

1. [What is an Algorithm?](#what-is-an-algorithm)
2. [Analyzing a Problem Statement](#analyzing-a-problem-statement)
3. [Developing an Algorithm](#developing-an-algorithm)
4. [Arithmetic Operations](#arithmetic-operations)
5. [Calculating Speed of an Object](#calculating-speed-of-an-object)
6. [Early Testing and Debugging Techniques](#early-testing-and-debugging-techniques)

### 1. **What is an Algorithm?**

An **algorithm** is a step-by-step procedure for solving a problem or completing a task. It outlines a set of instructions that should be followed to achieve a particular result. Algorithms are independent of programming languages, and they can be written in pseudocode or described in plain language before being implemented in a programming language.

In programming, algorithms form the core logic of how tasks are solved in code. For example, if you need to calculate the area of a rectangle, the algorithm might be:

1. **Start**
2. **Input** the length and width of the rectangle.
3. **Multiply** the length and width to get the area.
4. **Output** the area.
5. **End**

### 2. **Analyzing a Problem Statement**

To solve a problem using a program, the first step is **analyzing the problem statement**. This process involves breaking the problem down into smaller, manageable parts and identifying the necessary inputs and outputs.

Key steps in analyzing a problem:
1. **Identify the Inputs**: What data is given to you, and what information do you need to process?
2. **Identify the Outputs**: What results or outcomes should the program provide?
3. **Determine the Operations**: What steps or calculations are required to convert the inputs into the desired outputs?
4. **Clarify Assumptions**: Are there any specific conditions or constraints to consider (e.g., data types, limits)?

For example, consider the following problem:
Problem Statement: "Calculate the speed of an object given the time and distance."

- **Inputs**: Time, Distance
- **Outputs**: Speed
- **Operation**: Speed = Distance / Time

### 3. **Developing an Algorithm**

After analyzing the problem, we need to **develop an algorithm** to solve it. This involves outlining the sequence of steps needed to process the input and produce the output.

For the problem of calculating speed, the algorithm could look like this:

1. **Start**
2. **Input** the distance and time.
3. **Perform Calculation**: Divide the distance by time to calculate speed.
4. **Output** the calculated speed.
5. **End**

This algorithm can be implemented in Python as follows:

```python
# Step 1: Input values
distance = float(input("Enter the distance traveled (in meters): "))
time = float(input("Enter the time taken (in seconds): "))

# Step 2: Perform the calculation
speed = distance / time

# Step 3: Output the result
print("The speed of the object is", speed, "m/s")
```

### 4. **Arithmetic Operations**

In programming, **arithmetic operations** are essential for performing mathematical calculations. In Python, the following basic arithmetic operations are available:

- **Addition (`+`)**
- **Subtraction (`-`)**
- **Multiplication (`*`)**
- **Division (`/`)**
- **Exponentiation (`**`)**
- **Modulo (`%`)** (Remainder after division)

Example:
```python
a = 10
b = 5

# Perform arithmetic operations
sum_result = a + b  # Addition
diff_result = a - b  # Subtraction
prod_result = a * b  # Multiplication
quot_result = a / b  # Division
exp_result = a ** b  # Exponentiation
mod_result = a % b  # Modulo
```

### 5. **Calculating Speed of an Object**

To calculate the **speed** of an object, you can use the basic formula:
```
Speed = Distance / Time
```

This formula is used to determine how fast an object is moving based on the distance it travels over a specific period of time.

Example:
```python
# Inputs
distance = 100  # in meters
time = 20  # in seconds

# Calculation
speed = distance / time

# Output the result
print("Speed of the object is:", speed, "m/s")
```

In this example, the program calculates the speed of an object that travels 100 meters in 20 seconds, which results in a speed of 5 meters per second.

### 6. **Early Testing and Debugging Techniques**

**Testing** and **debugging** are crucial activities in programming to ensure that the program works as expected.

#### **Early Testing**
- **Test small parts of the program** as you write it. For example, test the calculation of speed immediately after implementing it.
- **Check for edge cases**: What happens if the time is 0? Test how the program behaves with different inputs, such as very large or very small values for time and distance.

#### **Debugging**
- If something goes wrong, use **print statements** to check intermediate values and make sure each part of the program is working as expected.
- **Check for syntax errors**, such as missing parentheses or incorrect variable names.
- Use Python's built-in error messages to help identify problems in your code.

Example with debugging using print statements:
```python
# Input values for distance and time
distance = float(input("Enter distance: "))
time = float(input("Enter time: "))

# Perform the calculation
speed = distance / time

# Debugging: Check the inputs and calculation result
print("Distance entered:", distance)
print("Time entered:", time)
print("Speed calculated:", speed)

# Output the result
print(f"Speed is {speed} meters per second.")
```