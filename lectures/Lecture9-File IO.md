# Lecture 9: File I/O

### **Table of Contents**

1. [Introduction to File I/O](#introduction-to-file-io)
2. [Working with TXT Files](#working-with-txt-files)
3. [Working with CSV Files](#working-with-csv-files)
4. [Reading an Array from a File](#reading-an-array-from-a-file)
5. [Debugging and Testing File I/O Operations](#debugging-and-testing-file-io-operations)

### 1. **Introduction to File I/O**

File **Input/Output (I/O)** operations allow programs to read from and write to external files. These operations are essential when you need to store data permanently or when your program needs to process data from a file.

In Python, file handling is done using built-in functions like **`open()`**, and file data can be read or written using different modes, such as `r` (read), `w` (write), and `a` (append).

Basic Syntax to open a file:
```python
file = open('filename.txt', 'r')  # Open the file in read mode
```

After opening the file, you can perform operations like reading its contents or writing to it, and then close the file using `file.close()`.

### 2. **Working with TXT Files**

**TXT files** are plain text files that contain unformatted data. Reading and writing to TXT files is straightforward in Python. You can read the entire contents of a file or read it line by line.

#### Reading from a TXT File:
To read from a TXT file, use the `open()` function in **read mode (`'r'`)**.

Example: Reading the contents of a TXT file:
```python
# Open the file in read mode
file = open('data.txt', 'r')

# Read the entire file content
content = file.read()
print(content)

# Close the file
file.close()
```

You can also read the file line by line:
```python
file = open('data.txt', 'r')

# Read each line of the file
for line in file:
    print(line.strip())  # .strip() removes any leading/trailing whitespace

file.close()
```

#### Writing to a TXT File:
To write data to a TXT file, open the file in **write mode (`'w'`)**.

Example: Writing to a file:
```python
file = open('output.txt', 'w')

# Write data to the file
file.write("Hello, World!\n")
file.write("This is a second line.")

file.close()
```

Note: If the file already exists, it will be overwritten. Use **append mode (`'a'`)** if you want to add data without overwriting.

### 3. **Working with CSV Files**

**CSV files** (Comma-Separated Values) are used to store tabular data in a text format. Each line represents a row, and the values within each row are separated by commas. CSV files are widely used for data storage and sharing.

To work with CSV files in Python, you can use the **`csv` module**. This module provides functions to read from and write to CSV files.

#### Reading from a CSV File:
The `csv.reader()` function is used to read a CSV file. It returns each row as a list of values.

Example: Reading from a CSV file:
```python
import csv

with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

In this example, `reader` is an iterable that yields each row of the CSV file as a list.

#### Writing to a CSV File:
The `csv.writer()` function is used to write data to a CSV file. You can pass a list of values, and the writer will convert them into a comma-separated format.

Example: Writing to a CSV file:
```python
import csv

with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    # Write header
    writer.writerow(['Name', 'Age', 'City'])
    # Write data
    writer.writerow(['Alice', 30, 'New York'])
    writer.writerow(['Bob', 25, 'Los Angeles'])
```

Note: Always specify `newline=''` when opening the file in write mode to avoid extra blank lines in the output.

### 4. **Reading an Array from a File**

You can store an array of data in a file and read it back into your program. Arrays are commonly represented in text files, and the data can be read and converted into an array or list in Python.

#### Reading an Array from a TXT File:
If you have a list of numbers in a TXT file (one number per line), you can read them into a list.

Example: Reading an array from a TXT file:
```python
# Assume 'numbers.txt' contains one number per line
with open('numbers.txt', 'r') as file:
    numbers = [int(line.strip()) for line in file]
    
print(numbers)
```

This code reads each line from the file, strips any leading or trailing whitespace, converts the line to an integer, and stores it in the `numbers` list.

#### Reading an Array from a CSV File:
If you have a CSV file containing numerical data, you can read it into a 2D array (list of lists) by treating each row as an array of values.

Example: Reading a 2D array from a CSV file:
```python
import csv

with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    array = [list(map(int, row)) for row in reader]  # Convert each row to a list of integers
    
print(array)
```

Here, the `map()` function is used to convert each string in the CSV row to an integer, and each row is added as a sublist in the final array.

### 5. **Debugging and Testing File I/O Operations**

When working with file I/O, it’s important to ensure that files are correctly opened, read, written, and closed. Below are some debugging techniques for handling file I/O operations:

#### Debugging File Opening:
Ensure that the file exists and that the correct file path is used.
```python
try:
    file = open('data.txt', 'r')
    content = file.read()
    print(content)
    file.close()
except FileNotFoundError:
    print("File not found.")
```

#### Debugging Data Parsing:
When reading data into arrays or lists, check that the data is correctly parsed. Use print statements to verify that the data read from the file matches the expected format.

Example:
```python
with open('numbers.txt', 'r') as file:
    numbers = [int(line.strip()) for line in file]
    print("Read numbers:", numbers)
```

Test with files containing edge cases, such as empty files or files with inconsistent formatting.

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

# Lecture 9: File I/O — Turning a Program Into a Data Processor

## 0. Why files?

Variables disappear when a program ends.

Files allow us to:

- store data;
- reload data;
- process experimental measurements;
- exchange data with other programs.

The key pipeline is:

```text
file
 ↓
read
 ↓
strings
 ↓
parse/convert
 ↓
Python data structure
 ↓
analyze
 ↓
output
```

## 1. Reading Text

Preferred modern pattern:

```python
with open("data.txt", "r") as file:
    content = file.read()
```

The `with` statement handles closing the file automatically.

For line-by-line processing:

```python
with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())
```

## 2. Why `strip()`?

A line read from a text file usually contains a newline.

```python
line = line.strip()
```

removes surrounding whitespace.

Do not confuse this with converting the value to a number.

```python
value = line.strip()
number = float(value)
```

Two separate operations:

```text
clean text
   ↓
convert type
```

## 3. Writing

```python
with open("output.txt", "w") as file:
    file.write("Experiment complete\n")
```

`"w"` can overwrite an existing file.

Use `"a"` to append.

## 4. CSV

CSV represents rows and columns.

```python
import csv

with open("data.csv", "r", newline="") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
```

Important:

> CSV values are read as strings unless you convert them.

For numeric data:

```python
values = [float(row[1]) for row in reader]
```

provided column 1 contains numeric values.

## 5. File-to-List Example

Suppose `numbers.txt` contains:

```text
10.5
11.2
9.8
```

Then:

```python
with open("numbers.txt") as file:
    numbers = [
        float(line.strip())
        for line in file
    ]
```

Now `numbers` is a list of floats.

## 6. Error Thinking

Possible failures include:

```text
FileNotFoundError
ValueError
PermissionError
```

These represent different problems.

For example:

```python
float("hello")
```

is a `ValueError`, not a file-opening problem.

## 7. Data Validation

A robust data-processing program should ask:

```text
Does the file exist?
Is the row format correct?
Are numeric fields actually numeric?
Are required columns present?
Are values within scientific limits?
```

## 8. Active-Learning Example

Consider:

```python
with open("data.txt") as file:
    numbers = [line.strip() for line in file]

average = sum(numbers) / len(numbers)
```

The file read succeeds. Why does the average fail?

Because `numbers` contains strings.

Correct:

```python
numbers = [
    float(line.strip())
    for line in file
]
```

## 9. CSV Challenge

Suppose:

```text
time,temperature
0,20.1
1,20.8
2,21.4
```

Write a program that:

1. reads the file;
2. skips the header;
3. stores times and temperatures separately;
4. finds the highest temperature;
5. reports the corresponding time.

Do not assume the first data row is the maximum.

## 10. Testing File Programs

Create small files representing:

- normal data;
- empty file;
- one-row file;
- malformed numeric value;
- missing file.

This is more informative than testing only the "happy path".
