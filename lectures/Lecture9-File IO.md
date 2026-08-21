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
