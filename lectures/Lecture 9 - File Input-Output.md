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
