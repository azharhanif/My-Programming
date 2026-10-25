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

#### 4.1 Can newline be something else?
Yes. Python's `open()` function has a newline parameter that controls how newline characters are handled when reading or writing a file.
```
Value	                  Behaviour when reading
newline=None	Default.   Python converts \r, \n, and \r\n into \n.
newline=""	             Python recognizes different newline styles but returns them untranslated.
newline="\n"	           Only \n is treated as a line ending; other newline styles are not translated.
newline="\r"	           Only \r is treated as a line ending.
newline="\r\n"	         Only \r\n is treated as a line ending.
```
Here, `\n` represents a line feed, `\r` represents a carriage return, and `\r\n` is the traditional Windows line-ending sequence.

These are all valid examples:
```
open("sample_students.csv", "r", newline=None)
open("sample_students.csv", "r", newline="")
open("sample_students.csv", "r", newline="\n")
open("sample_students.csv", "r", newline="\r\n")
```
However, for CSV files, the recommended practice is:
```
with open("sample_students.csv", "r", newline="") as file:
```
When writing CSV files, the same setting is important:
```
import csv

with open("output.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["student_id", "name", "score"])
    writer.writerow([1001, "Amina", 87])
```
**Takeaway:** `newline=""` does not remove newlines. 

It disables Python's automatic newline translation so the csv module can handle them correctly.
#### 4.2 Why does the CSV module recommend newline=""?
Consider this CSV file:
```
student_id,name,comment
1001,Amina,"Likes Python
and data science"
1002,Daniel,"Enjoys programming"
```
Notice that Amina's comment spans two physical lines, but it belongs to one CSV record.

When you write:
```
import csv

with open("sample_students.csv", "r", newline="") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
```
The CSV reader can correctly interpret the line break inside the quoted field.

If you omit `newline=""`, Python's default newline conversion can interfere with the CSV module's handling of newline characters.

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
#### 7.1. Example: CSV file with missing values
Suppose sample_students.csv contains:
```
student_id,name,program,score
1001,Amina,Science,87
1002,Daniel,Computer Science,
1003,Sofia,,78
1004,Marcus,Computer Science,85
1005,Leila,Science,95
```
There are two missing values:
- Daniel has no score.
- Sofia has no program.
  
When reading with csv.reader(), Python represents an empty CSV field as an empty string "".
```
import csv
with open("sample_students.csv", "r", newline="") as file:
     reader = csv.reader(file)
     for row in reader:
        print(row)
```
For Daniel, the output is:
```
['1002', 'Daniel', 'Computer Science', '']

```
Notice that the missing score is '', not None and not 0.
#### 7.2. Check for empty strings
This is the simplest method.
```
import csv

with open("sample_students.csv", "r", newline="") as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header

    for row in reader:
        student_id = row[0]
        name = row[1]
        program = row[2]
        score_text = row[3]

        if score_text == "":
            print(name, "has no recorded score")
        else:
            score = float(score_text)
            print(name, "scored", score)
```
This avoids trying to convert an empty string to a number, which would cause a `ValueError`.

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
