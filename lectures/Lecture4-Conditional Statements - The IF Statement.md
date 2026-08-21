# Lecture 4: Conditional Statements - The IF Statement

### **Table of Contents**

1. [Introduction to Conditional Statements](#introduction-to-conditional-statements)
2. [The If Statement](#the-if-statement)
3. [Comparisons and Logical Operators](#comparisons-and-logical-operators)
4. [Using If Statements in Python](#using-if-statements-in-python)
5. [Debugging and Testing Conditional Statements](#debugging-and-testing-conditional-statements)

### 1. **Introduction to Conditional Statements**

**Conditional statements** allow programs to make decisions based on specific conditions. These statements let you execute different parts of code depending on whether certain conditions are true or false. In programming, this is crucial for implementing logic that changes the flow of execution based on the inputs or data.

The most common **conditional statement** is the **if statement**, which allows you to run a block of code only if a condition is met.

### 2. **The If Statement**

The **if statement** is used to check if a condition is **true**. If the condition is true, the program will execute the block of code inside the if statement. If the condition is false, the program will skip that block and continue with the rest of the code.

The basic structure of an **if statement** is:

```python
if condition:
    # Code to execute if the condition is true
```

#### Syntax:
- **condition**: This is an expression that evaluates to `True` or `False`.
- **Code block**: The indented code under the `if` statement is executed only if the condition is true.

Example:
```python
age = 18

if age >= 18:
    print("You are an adult.")
```

In this example, the condition `age >= 18` evaluates to `True`, so the message "You are an adult." is printed.

### 3. **Comparisons and Logical Operators**

To create useful **conditions**, we use **comparison operators** to compare values. These operators allow us to compare two values and return a Boolean result (`True` or `False`):

- **Equal to (`==`)**: Checks if two values are equal.
- **Not equal to (`!=`)**: Checks if two values are not equal.
- **Greater than (`>`)**: Checks if the left value is greater than the right.
- **Less than (`<`)**: Checks if the left value is less than the right.
- **Greater than or equal to (`>=`)**: Checks if the left value is greater than or equal to the right.
- **Less than or equal to (`<=`)**: Checks if the left value is less than or equal to the right.

Example:
```python
a = 5
b = 3

if a > b:
    print("a is greater than b")
```

Additionally, **logical operators** can combine multiple conditions:
- **and**: Returns `True` if both conditions are true.
- **or**: Returns `True` if at least one condition is true.
- **not**: Reverses the result of a condition.

Example with logical operators:
```python
age = 20
has_permission = True

if age >= 18 and has_permission:
    print("You are allowed to enter.")
```

In this example, both conditions must be true for the message to be printed.

### 4. **Using If Statements in Python**

In Python, the **if statement** can be expanded with **else** and **elif** (else if) to check multiple conditions.

- **if**: Checks the first condition.
- **elif**: Checks additional conditions if the first condition is false.
- **else**: Executes code if all conditions are false.

Example:
```python
age = 15

if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")
```

Here:
- If `age` is 18 or greater, the program will print "You are an adult."
- If `age` is between 13 and 17, the program will print "You are a teenager."
- Otherwise, the program will print "You are a child."

### 5. **Debugging and Testing Conditional Statements**

When working with **if statements**, it's important to test different conditions to ensure the code behaves as expected. 

#### Debugging with Print Statements
- **Print statements** can be used to verify whether certain conditions are being met and to check the flow of execution.
- You can print values before the `if` statement to verify the condition or inside the `if` block to ensure that it is executing.

Example:
```python
age = 20

# Debugging: Check if the condition is met
print("Checking if the person is an adult.")

if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult.")
```

#### Testing Different Conditions
Make sure to test **edge cases**, such as:
- If the condition checks boundaries (e.g., checking if `age == 18`).
- If the **else** and **elif** blocks are triggered correctly when conditions are false.

Example of testing different conditions:
```python
age = 18

if age > 18:
    print("You are older than 18.")
elif age == 18:
    print("You are exactly 18.")
else:
    print("You are younger than 18.")
```

Test this code with different values of `age` to ensure all conditions are covered.

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

# Lecture 4: Conditional Statements — Making Decisions

## 0. Why conditions matter

A scientific program often needs to choose what to do:

```text
Is the temperature above the safe limit?
Is the velocity positive?
Is a measurement inside the acceptable range?
Is the denominator zero?
```

An `if` statement turns a Boolean condition into program behavior.

## 1. Predict Before Running

```python
temperature = 20

if temperature > 20:
    print("hot")
elif temperature == 20:
    print("exactly 20")
else:
    print("cold")
```

Predict the output.

Now change `20` to:

```text
19
20
21
```

What changes?

## 2. Comparison Operators

```python
==  !=  >  <  >=  <=
```

Important distinction:

```python
x = 10      # assignment
x == 10     # comparison
```

## 3. Boolean Conditions

```python
temperature = 22
humidity = 40

if temperature > 20 and humidity < 60:
    print("condition acceptable")
```

Think of `and` as requiring both conditions.

```python
if temperature > 30 or humidity > 80:
    print("warning")
```

At least one condition must be true.

```python
if not sensor_available:
    print("Cannot collect data")
```

## 4. Boundary Thinking

Suppose the acceptable temperature range is 18 through 25 inclusive.

Correct:

```python
if 18 <= temperature <= 25:
    print("acceptable")
```

This is clearer than:

```python
if temperature >= 18 and temperature <= 25:
```

Both work, but the first communicates the range directly.

## 5. A Tricky Ordering Problem

Consider:

```python
score = 85

if score >= 50:
    print("pass")
elif score >= 80:
    print("excellent")
```

What prints?

Why does `"excellent"` never print?

The conditions are checked from top to bottom. A condition that is too broad can prevent later branches from being reached.

Correct ordering:

```python
if score >= 80:
    print("excellent")
elif score >= 50:
    print("pass")
else:
    print("fail")
```

## 6. Scientific Decision Example

```python
velocity = -4.2

if velocity > 0:
    direction = "positive"
elif velocity < 0:
    direction = "negative"
else:
    direction = "zero"

print(direction)
```

Separate the **classification** from the output when possible.

## 7. Debugging Conditions

For a complicated condition:

```python
if age >= 18 and has_id and not suspended:
```

temporarily inspect the pieces:

```python
print(age >= 18)
print(has_id)
print(not suspended)
```

This helps locate which assumption failed.

## 8. Active-Learning Questions

1. What is wrong with using `=` instead of `==`?
2. Why does branch order matter?
3. How would you test a condition whose valid range is `0 <= x <= 1`?
4. Why are boundary values especially important?
5. Write a condition for "temperature is below 0 OR above 100."

## 9. Mini Challenge

Ask for a temperature and classify it as:

```text
below freezing       < 0
freezing point       == 0
liquid range         0 < T < 100
boiling point        == 100
above boiling        > 100
```

Test exactly:

```text
-1, 0, 25, 100, 101
```

Explain why these five tests are better than testing only `25`.
