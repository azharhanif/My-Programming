# Student Lab: Your First Pytest Tests in VS Code

## Purpose

In this lab you will learn how to use **pytest** to test Python programs
in Visual Studio Code (VS Code).

The goal is to learn this complete cycle:

> **Write code → Predict → Write a test → Run pytest → Read the result →
> Debug → Fix → Test again**

By the end you should be able to: - install and run pytest; - write a
simple pytest test; - understand `assert`; - recognize passing and
failing tests; - read a pytest failure message; - add test cases; - run
tests from the VS Code Testing interface; - understand basic pytest test
discovery.

------------------------------------------------------------------------

## Step 1 --- Create a VS Code Project

Create a folder named:

``` text
pytest_lab
```

Open it in VS Code.

Your project will eventually contain:

``` text
pytest_lab/
    calculator.py
    test_calculator.py
```

Open **Terminal → New Terminal**.

Checkpoint: make sure the terminal is inside your `pytest_lab` folder.

------------------------------------------------------------------------

## Step 2 --- Check Python

Run:

``` bash
python --version
```

If necessary, try:

``` bash
python3 --version
```

### Think

What does this command tell you?

**Expected idea:** It tells you which Python version the terminal is
using.

------------------------------------------------------------------------

## Step 3 --- Install pytest

Run:

``` bash
python -m pip install pytest
```

If you use `python3`:

``` bash
python3 -m pip install pytest
```

Then verify:

``` bash
python -m pytest --version
```

You should see a pytest version.

### Why use `python -m pip`?

It makes clear which Python interpreter is installing pytest.

------------------------------------------------------------------------

## Step 4 --- Write Your First Function

Create `calculator.py`:

``` python
def add(a, b):
    return a + b
```

### Before running anything, answer:

1.  What are the inputs?
2.  What is the output?
3.  What should `add(2, 3)` return?
4.  What should `add(10, 7)` return?

Write your predictions in your lab notes.

------------------------------------------------------------------------

## Step 5 --- Write Your First Pytest Test

Create `test_calculator.py`:

``` python
from calculator import add


def test_add():
    assert add(2, 3) == 5
```

### Understand this line

``` python
assert add(2, 3) == 5
```

It means:

> I expect `add(2, 3)` to equal `5`.

If the expression is true, the test passes.

If it is false, the test fails.

------------------------------------------------------------------------

## Step 6 --- Run pytest

In the terminal:

``` bash
python -m pytest
```

You should see a result containing:

``` text
1 passed
```

The exact formatting depends on your pytest version.

### What does the `.` mean?

A dot represents a passing test.

------------------------------------------------------------------------

## Step 7 --- Deliberately Break the Test

Change:

``` python
assert add(2, 3) == 5
```

to:

``` python
assert add(2, 3) == 6
```

Do **not** change `calculator.py`.

Run:

``` bash
python -m pytest
```

The test should fail.

Look for information similar to:

``` text
E       assert 5 == 6
```

### Your task

Identify:

-   the actual result;
-   the expected result;
-   the line where the test failed.

------------------------------------------------------------------------

## Step 8 --- Decide What Is Wrong

Ask yourself:

> Is the Python function wrong, or is my test expectation wrong?

Here the function produces:

``` text
5
```

The test expects:

``` text
6
```

Therefore the **test expectation is wrong**.

### Important lesson

A failing test does not automatically mean that the program is wrong.

The test itself can be wrong.

------------------------------------------------------------------------

## Step 9 --- Fix the Test

Change the test back to:

``` python
assert add(2, 3) == 5
```

Run:

``` bash
python -m pytest
```

Expected:

``` text
1 passed
```

------------------------------------------------------------------------

## Step 10 --- Add More Tests

Add:

``` python
def test_add_zero():
    assert add(5, 0) == 5


def test_add_negative():
    assert add(10, -3) == 7


def test_add_two_negative_numbers():
    assert add(-4, -6) == -10
```

Run:

``` bash
python -m pytest
```

Expected:

``` text
4 passed
```

### Think

Why is it useful to test more than one input?

Write your answer.

------------------------------------------------------------------------

## Step 11 --- Use VS Code's Testing Interface

Open the Command Palette:

``` text
Ctrl + Shift + P
```

Search for:

``` text
Python: Configure Tests
```

Choose **pytest** and select the current project folder when prompted.

Then open the **Testing** view in the Activity Bar.

You should be able to see your test file and test functions.

You can run: - all tests; - one test; - tests in one file.

> The exact wording of VS Code menus may vary slightly by version.

### Important

VS Code is not replacing pytest.

It is providing a graphical interface for running and viewing pytest
tests.

------------------------------------------------------------------------

## Step 12 --- Understand Test Discovery

Pytest normally discovers files such as:

``` text
test_calculator.py
```

and functions such as:

``` python
def test_add():
```

### Experiment

Rename:

``` text
test_calculator.py
```

to:

``` text
calculator_tests.py
```

Run:

``` bash
python -m pytest
```

Observe the result.

Then rename it back to:

``` text
test_calculator.py
```

Run pytest again.

### Question

Why did the filename matter?

------------------------------------------------------------------------

## Step 13 --- Add a Second Function

Add this to `calculator.py`:

``` python
def square(number):
    return number * number
```

Before testing, predict:

``` text
square(4)
square(0)
square(-3)
```

------------------------------------------------------------------------

## Step 14 --- Test `square`

Change the import to:

``` python
from calculator import add, square
```

Then add:

``` python
def test_square():
    assert square(4) == 16


def test_square_zero():
    assert square(0) == 0


def test_square_negative():
    assert square(-3) == 9
```

Run:

``` bash
python -m pytest
```

Expected:

``` text
7 passed
```

------------------------------------------------------------------------

## Step 15 --- Debug a Broken Function

Temporarily change:

``` python
def square(number):
    return number * number
```

to:

``` python
def square(number):
    return number + number
```

Do not change the tests.

Run:

``` bash
python -m pytest
```

### Answer these questions

1.  Which test failed?
2.  What value was expected?
3.  What value was actually produced?
4.  Which line of the program caused the problem?
5.  How should you fix it?

Then restore:

``` python
def square(number):
    return number * number
```

Run pytest again.

------------------------------------------------------------------------

## Step 16 --- Common Problems

### `pytest` is not recognized

Use:

``` bash
python -m pytest
```

### `No module named pytest`

Install it:

``` bash
python -m pip install pytest
```

### `no tests ran`

Check: - filename starts with `test_`; - test function starts with
`test_`; - terminal is in the correct project folder.

### Import error

Make sure these files are in the same folder:

``` text
calculator.py
test_calculator.py
```

------------------------------------------------------------------------

# Final Mini-Challenge

Create:

``` python
def is_even(number):
    # Return True if number is even.
    # Return False otherwise.
```

### A --- Predict

Predict:

``` text
is_even(4)
is_even(7)
is_even(0)
is_even(-2)
```

### B --- Code

Implement the function.

### C --- Test

Write at least four pytest tests.

Include: - a positive even number; - a positive odd number; - zero; - a
negative number.

### D --- Break and Debug

Temporarily introduce an error.

Run pytest.

Read the failure.

Fix the function.

Run pytest again.

### E --- Explain

In your own words:

> What is the difference between running a Python program and running a
> pytest test?

------------------------------------------------------------------------

# Final Check

You should now be able to explain:

-   What is pytest?
-   What does `assert` do?
-   What does `1 passed` mean?
-   What does a failed test tell you?
-   Why test several inputs?
-   Why do filenames and function names matter?
-   How do you run pytest from the terminal?
-   How do you run pytest from VS Code?
-   Can a test itself be wrong?
-   How can pytest help you debug?

## Key Idea

> **A test is an executable expectation.**

The workflow is:

> **Predict → Code → Test → Read failure → Debug → Fix → Retest**
