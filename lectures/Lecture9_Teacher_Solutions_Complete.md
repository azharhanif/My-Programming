# Lecture 9 — File I/O
## Complete Teacher Solutions and Answers to Activity Questions

This document provides a complete worked solution for all eight practice activities,
including answers to the conceptual questions, expected output, and teaching notes.

The solutions use:
- `open()` and `with open(...)`
- `read()`, line-by-line reading, and `strip()`
- writing with `"w"` and `"a"`
- the built-in `csv` module and `csv.reader()`
- lists, loops, indexes, and type conversion
- `try` / `except` for expected errors

---

## 1. Project folder setup

Place the Python file and the supplied `data` folder in the same project folder:

```text
Lecture9/
├── Lecture9_Solutions.py
└── data/
    ├── temperatures.txt
    ├── numbers_with_spaces.txt
    ├── student_scores.csv
    ├── student_scores_missing.csv
    ├── lab_readings.csv
    ├── messy_measurements.csv
    ├── comments_multiline.csv
    └── inventory.csv
```

Run the program from inside the `Lecture9` folder. The examples use relative paths
such as `data/temperatures.txt`.

The `lab_readings.csv` file is included as an additional practice dataset. It is not
required by the eight activities below.

---

# Activity 1 — Read, clean, and convert text data

**Files:** `temperatures.txt` and `numbers_with_spaces.txt`

### Complete solution

```python
def read_numeric_lines(filename):
    values = []

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            cleaned_line = line.strip()

            if cleaned_line == "":
                continue

            number = float(cleaned_line)
            values.append(number)

    return values


def display_statistics(values):
    if len(values) == 0:
        print("No numeric readings were found.")
        return

    total = sum(values)
    average = total / len(values)

    print("Values:", values)
    print("Number of readings:", len(values))
    print("Minimum:", min(values))
    print("Maximum:", max(values))
    print("Average:", round(average, 3))


# Part A
temperatures = read_numeric_lines("data/temperatures.txt")
print("TEMPERATURE READINGS")
display_statistics(temperatures)

# Part B
numbers = read_numeric_lines("data/numbers_with_spaces.txt")
print("\nNUMBERS WITH SPACES AND BLANK LINES")
display_statistics(numbers)
```

### Expected results

**`temperatures.txt`**

```text
Values: [20.5, 21.0, 19.8, 22.4, 20.9]
Number of readings: 5
Minimum: 19.8
Maximum: 22.4
Average: 20.92
```

**`numbers_with_spaces.txt`**

```text
Values: [10.5, 11.2, 9.8, 12.0]
Number of readings: 4
Minimum: 9.8
Maximum: 12.0
Average: 10.875
```

### Answers to the questions

**1. Why is `strip()` needed before conversion?**

`strip()` removes leading and trailing whitespace, including newline characters
(`\n`), spaces, and tabs. It ensures that the text is clean before conversion.
For example, `"  10.5  "` becomes `"10.5"`.

Python can convert some strings containing surrounding spaces to floats, but using
`strip()` makes the cleaning step explicit and also allows us to detect blank lines.

**2. Why should the blank line be skipped?**

After calling `strip()`, a blank line becomes an empty string: `""`. Calling
`float("")` raises a `ValueError`. We skip the line so that the program does not
attempt an invalid conversion.

**3. What is the difference between a string such as `"20.5"` and the float `20.5`?**

`"20.5"` is text (`str`). It represents characters and cannot be used directly
for numerical arithmetic. `20.5` is a floating-point number (`float`) and can be
used in calculations such as addition, division, and averaging. We convert the
string using `float("20.5")`.

---

# Activity 2 — Write a report to a file

**Input:** The temperature values from Activity 1.

### Complete solution

```python
temperatures = []

with open("data/temperatures.txt", "r", encoding="utf-8") as file:
    for line in file:
        cleaned_line = line.strip()

        if cleaned_line != "":
            temperatures.append(float(cleaned_line))

if len(temperatures) > 0:
    average = sum(temperatures) / len(temperatures)

    # Write mode: creates the file or replaces its previous contents.
    with open("temperature_report.txt", "w", encoding="utf-8") as report:
        report.write("TEMPERATURE REPORT\n")
        report.write("==================\n")
        report.write(f"Number of readings: {len(temperatures)}\n")
        report.write(f"Minimum temperature: {min(temperatures):.1f} C\n")
        report.write(f"Maximum temperature: {max(temperatures):.1f} C\n")
        report.write(f"Average temperature: {average:.2f} C\n")

    # Read the report back and display it.
    with open("temperature_report.txt", "r", encoding="utf-8") as report:
        print(report.read())
else:
    print("No readings available. No report was created.")
```

### Expected report

The program creates `temperature_report.txt` in the project folder:

```text
TEMPERATURE REPORT
==================
Number of readings: 5
Minimum temperature: 19.8 C
Maximum temperature: 22.4 C
Average temperature: 20.92 C
```

### Answer to the extension question

**What is the difference between overwrite and append?**

- `"w"` means *write*. It creates a new file if one does not exist. If the file
  already exists, its previous contents are erased before the new content is written.
- `"a"` means *append*. It creates the file if necessary, but if the file already
  exists, new content is added to the end. Existing content is preserved.

For example:

```python
# Overwrites the file.
with open("temperature_report.txt", "w", encoding="utf-8") as file:
    file.write("New report\n")

# Adds a line to the end of the existing file.
with open("temperature_report.txt", "a", encoding="utf-8") as file:
    file.write("This line was appended.\n")
```

**Teaching note:** Have students run the `"w"` version twice and inspect the file.
Then have them run the `"a"` version twice. This makes the difference observable.

---

# Activity 3 — Read a CSV file and calculate class results

**File:** `student_scores.csv`

### Complete solution

```python
import csv

names = []
scores = []

with open("data/student_scores.csv",
          "r", encoding="utf-8", newline="") as file:

    reader = csv.reader(file)

    header = next(reader)  # Skip the header row.
    print("Columns:", header)

    for row in reader:
        name = row[1]
        score = float(row[3])

        names.append(name)
        scores.append(score)

if len(scores) > 0:
    average = sum(scores) / len(scores)
    highest_score = max(scores)
    lowest_score = min(scores)

    print("Scores:", scores)
    print("Class average:", round(average, 2))
    print("Highest score:", highest_score)
    print("Lowest score:", lowest_score)

    highest_index = scores.index(highest_score)
    print("Highest-scoring student:", names[highest_index])
else:
    print("No scores were found.")
```

### Expected results

```text
Scores: [87.0, 91.0, 78.0, 85.0, 95.0]
Class average: 87.2
Highest score: 95.0
Lowest score: 78.0
Highest-scoring student: Leila
```

### Answers to the questions

**1. Why does `csv.reader()` return strings?**

CSV files store information as text. The CSV reader separates each record into
fields but does not decide whether a field represents an integer, a float, a date,
or ordinary text. Therefore, values such as `"87"` are returned as strings.
The programmer must convert numeric fields when numerical calculations are needed.

**2. Why do we call `next(reader)`?**

The first row contains column headings:

```text
student_id,name,program,score
```

We call `next(reader)` to consume and skip that header row. Without this step,
the loop would treat `"score"` as a data value and `float("score")` would raise
a `ValueError`.

**3. What does `row[3]` refer to?**

`row` is a list containing the fields from one CSV record. List indexing begins
at zero:

| Index | Field |
|---:|---|
| `row[0]` | student ID |
| `row[1]` | name |
| `row[2]` | program |
| `row[3]` | score |

Therefore, `row[3]` is the fourth field, which contains the student's score.

**Teaching note:** Emphasize that `row[3]` is an index in a list, not a column
name. The CSV reader does not automatically create named fields.

---

# Activity 4 — Detect missing CSV values

**File:** `student_scores_missing.csv`

### Complete solution

```python
import csv

available_scores = []
missing_program_count = 0
missing_score_count = 0

with open("data/student_scores_missing.csv",
          "r", encoding="utf-8", newline="") as file:

    reader = csv.reader(file)
    next(reader)  # Skip the header.

    for row in reader:
        student_id = row[0]
        name = row[1]
        program = row[2]
        score_text = row[3]

        if program == "":
            missing_program_count += 1
            print(name, "is missing a program.")

        if score_text == "":
            missing_score_count += 1
            print(name, "is missing a score.")
        else:
            available_scores.append(float(score_text))

print("Missing program count:", missing_program_count)
print("Missing score count:", missing_score_count)
print("Available score count:", len(available_scores))

if len(available_scores) > 0:
    average = sum(available_scores) / len(available_scores)
    print("Average of available scores:", round(average, 2))
else:
    print("No scores are available.")
```

### Expected results

- Daniel (ID 1002) is missing a score.
- Sofia (ID 1003) is missing a program.
- Available scores: `[87.0, 78.0, 85.0, 95.0]`
- Missing program count: `1`
- Missing score count: `1`
- Available score count: `4`
- Average of available scores: `86.25`

### Teaching explanation

An empty CSV field is represented by an empty string, `""`. It is not automatically
converted to zero, `None`, or another special value.

The program checks for an empty score before calling `float()`. This order matters:
`float("")` would raise a `ValueError`.

A missing score should not be silently treated as zero. A zero is a real numerical
score; a missing value means no score was recorded. They have different meanings.

---

# Activity 5 — Validate measurements before calculating

**File:** `messy_measurements.csv`

The acceptable experimental range is greater than 0 and less than or equal to
20 grams.

### Complete solution

```python
import csv

accepted_masses = []

with open("data/messy_measurements.csv",
          "r", encoding="utf-8", newline="") as file:

    reader = csv.reader(file)
    next(reader)  # Skip the header.

    for row in reader:
        sample_id = row[0]
        mass_text = row[1]

        # Check for a missing field first.
        if mass_text == "":
            print(sample_id, "has a missing mass value.")
            continue

        # Check whether the text can be converted to a number.
        try:
            mass = float(mass_text)
        except ValueError:
            print(sample_id, "contains invalid numeric text:", mass_text)
            continue

        # Check whether the numeric value makes sense for this experiment.
        if mass <= 0 or mass > 20:
            print(sample_id, "is outside the acceptable range:", mass)
            continue

        accepted_masses.append(mass)
        print(sample_id, "accepted:", mass, "g")

print("Accepted masses:", accepted_masses)

if len(accepted_masses) > 0:
    average = sum(accepted_masses) / len(accepted_masses)
    print("Number of accepted readings:", len(accepted_masses))
    print("Average accepted mass:", round(average, 3), "g")
else:
    print("No valid measurements were found.")
```

### Expected results

| Sample | Input | Result | Reason |
|---|---:|---|---|
| S01 | 12.5 | Accepted | Numeric and within range |
| S02 | 11.8 | Accepted | Numeric and within range |
| S03 | blank | Rejected | Missing value |
| S04 | `not_available` | Rejected | Cannot convert to float |
| S05 | 13.1 | Accepted | Numeric and within range |
| S06 | 999.0 | Rejected | Numeric but outside experimental range |
| S07 | 12.9 | Accepted | Numeric and within range |

Accepted values:

```text
[12.5, 11.8, 13.1, 12.9]
```

Average:

\[
\frac{12.5 + 11.8 + 13.1 + 12.9}{4} = 12.575
\]

The average accepted mass is **12.575 g**.

### Answers to the questions

**1. Which problem is detected by checking for `""`?**

It detects a missing or empty field. In this dataset, sample S03 has no mass
recorded. The field is an empty string, so the program reports it as missing.

**2. Which problem is detected by `except ValueError`?**

It detects text that cannot be converted to a floating-point number. For example,
`float("not_available")` raises `ValueError`, so sample S04 is rejected.

**3. Why is `999.0` not a conversion error, even though it is not acceptable here?**

`"999.0"` is valid numeric text. Python can convert it successfully to the float
`999.0`. The problem is not its data type or numeric format; it is that the value
does not satisfy the experiment's acceptable range. This is a *domain validation*
problem, not a type-conversion problem.

**4. Why must the acceptable range come from knowledge of the experiment?**

A program cannot decide whether a measurement is realistic without understanding
what is being measured. A mass between 0 and 20 grams may be reasonable for a
small object, but not for a large object. The acceptable range must come from
the scientific or practical context, not from an arbitrary programming rule.

### Key distinction for students

There are three different checks:

1. **Missing-value check:** Is the field empty?
2. **Conversion check:** Can the text be converted to a number?
3. **Domain check:** Is the number realistic and acceptable for this problem?

Passing one check does not guarantee that the value passes the next one.

---

# Activity 6 — CSV records with a line break inside a field

**File:** `comments_multiline.csv`

### Complete solution

```python
import csv

record_count = 0

with open("data/comments_multiline.csv",
          "r", encoding="utf-8", newline="") as file:

    reader = csv.reader(file)
    next(reader)  # Skip the header.

    for row in reader:
        student_id = row[0]
        name = row[1]
        comment = row[2]

        record_count += 1

        print("\nStudent ID:", student_id)
        print("Name:", name)
        print("Comment:")
        print(comment)

print("\nNumber of student records:", record_count)
```

### Expected result

There are **3 student records**:

- Amina — comment spans two physical lines.
- Daniel — one-line comment.
- Sofia — one-line comment.

The line break inside Amina's quoted comment is part of the field. It does not
create a new CSV record.

### Answer to the question

**Why is it safer to let `csv.reader()` identify records than to split the file manually at every newline?**

A CSV field can contain a line break when the field is enclosed in quotation
marks. Splitting the file manually at every newline would incorrectly divide
Amina's comment into two pieces and could make the program treat one student as
two records.

`csv.reader()` understands CSV quoting rules and recognizes that the embedded
newline belongs to the same field and record. It is therefore safer and more
reliable than manually splitting the file into lines and then splitting each
line at commas.

**Teaching note:** This is one reason to use the CSV module rather than trying
to parse CSV files with `line.split(",")`.

---

# Activity 7 — Create an inventory summary

**File:** `inventory.csv`

### Complete solution

```python
import csv

item_names = []
inventory_values = []

with open("data/inventory.csv",
          "r", encoding="utf-8", newline="") as file:

    reader = csv.reader(file)
    next(reader)  # Skip the header.

    for row in reader:
        item = row[0]
        quantity = int(row[1])
        unit_price = float(row[2])

        item_value = quantity * unit_price

        item_names.append(item)
        inventory_values.append(item_value)

        print(
            item, ":", quantity, "x $",
            format(unit_price, ".2f"), "= $",
            format(item_value, ".2f"),
            sep=""
        )

total_inventory_value = sum(inventory_values)
print("\nTotal inventory value: $", format(total_inventory_value, ".2f"), sep="")

if len(inventory_values) > 0:
    highest_index = inventory_values.index(max(inventory_values))

    print(
        "Item with greatest inventory value:",
        item_names[highest_index]
    )
    print(
        "Its inventory value: $",
        format(inventory_values[highest_index], ".2f"),
        sep=""
    )
```

### Expected results

| Item | Quantity | Unit price | Inventory value |
|---|---:|---:|---:|
| Pencils | 24 | $0.50 | $12.00 |
| Notebooks | 12 | $2.75 | $33.00 |
| Markers | 8 | $1.80 | $14.40 |
| Folders | 15 | $1.25 | $18.75 |
| **Total** | | | **$78.15** |

The item with the greatest inventory value is **Notebooks**, at **$33.00**.

### Teaching explanation

The two lists are *parallel lists*:

```python
item_names = ["Pencils", "Notebooks", "Markers", "Folders"]
inventory_values = [12.0, 33.0, 14.4, 18.75]
```

The value at a particular index in one list corresponds to the value at the same
index in the other list. For example, index `1` identifies `"Notebooks"` and
`33.0`.

The program finds the index of the largest inventory value, then uses that same
index to retrieve the matching item name.

---

# Activity 8 — File I/O testing challenge

The program must handle normal files, empty files, blank-only files, malformed
numeric values, missing files, and files with one valid value.

### Complete solution

```python
from pathlib import Path


def process_numeric_file(filename):
    values = []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                cleaned_line = line.strip()

                if cleaned_line == "":
                    continue

                try:
                    number = float(cleaned_line)
                    values.append(number)
                except ValueError:
                    print(
                        "Line", line_number,
                        "contains invalid numeric data:",
                        cleaned_line,
                        "- skipped"
                    )

    except FileNotFoundError:
        print("Error: file was not found:", filename)
        return
    except OSError as error:
        print("File access error:", error)
        return

    if len(values) == 0:
        print("The file contains no valid numeric values.")
        return

    average = sum(values) / len(values)

    print("Valid values:", values)
    print("Number of valid values:", len(values))
    print("Minimum:", min(values))
    print("Maximum:", max(values))
    print("Average:", round(average, 3))


# Create test files for the demonstration.
test_folder = Path("activity_8_tests")
test_folder.mkdir(exist_ok=True)

with open(test_folder / "normal.txt", "w", encoding="utf-8") as file:
    file.write("3.5\n4.0\n5.5\n")

with open(test_folder / "empty.txt", "w", encoding="utf-8") as file:
    pass

with open(test_folder / "blank_only.txt", "w", encoding="utf-8") as file:
    file.write("   \n\n\t\n")

with open(test_folder / "malformed.txt", "w", encoding="utf-8") as file:
    file.write("10\nhello\n12.5\n")

with open(test_folder / "one_value.txt", "w", encoding="utf-8") as file:
    file.write("7.25\n")


# Run all six test cases.
test_filenames = [
    "normal.txt",
    "empty.txt",
    "blank_only.txt",
    "malformed.txt",
    "missing.txt",
    "one_value.txt"
]

for filename in test_filenames:
    print("\nTESTING:", filename)
    process_numeric_file(test_folder / filename)
```

### Expected behavior for each test case

| Test file | Expected behavior |
|---|---|
| `normal.txt` | Reads 3.5, 4.0, and 5.5; calculates statistics |
| `empty.txt` | Reports that there are no valid numeric values |
| `blank_only.txt` | Skips blank lines and reports no valid numeric values |
| `malformed.txt` | Reports and skips `hello`; processes 10 and 12.5 |
| `missing.txt` | Catches `FileNotFoundError` and displays a clear message |
| `one_value.txt` | Processes 7.25; minimum, maximum, and average are all 7.25 |

### Expected numerical results

**`normal.txt`**

- Values: `[3.5, 4.0, 5.5]`
- Count: `3`
- Minimum: `3.5`
- Maximum: `5.5`
- Average: `4.333`

**`malformed.txt`**

- Valid values: `[10.0, 12.5]`
- Invalid text: `hello`
- Count: `2`
- Minimum: `10.0`
- Maximum: `12.5`
- Average: `11.25`

**`one_value.txt`**

- Values: `[7.25]`
- Count: `1`
- Minimum: `7.25`
- Maximum: `7.25`
- Average: `7.25`

### Teaching explanation

The solution uses two levels of exception handling:

- The outer `try` / `except` handles problems opening or accessing the file,
  especially `FileNotFoundError`.
- The inner `try` / `except` handles a line that cannot be converted to a float.

The program does not use a broad `except:` clause. It catches the expected
exceptions and handles them at the appropriate level.

The program also checks whether the list is empty before calculating the average.
This prevents division by zero.

---

# Final reflection — Model answer

**Question:** Explain the full file-processing pipeline:

```text
file → read → strings → clean/validate → convert → store → analyze → report
```

**Model answer (one possible response):**

A program first opens a file and reads its contents. The data is initially read
as strings, so the program must clean the text by removing whitespace and checking
for missing or invalid values. Numeric strings are then converted to the appropriate
numeric types, such as `int` or `float`, before being stored in lists. The program
can analyze the stored values by calculating totals, averages, minimums, or maximums,
and finally display the results or write them to an output file. Errors can occur
at every stage, such as an incorrect file path, an empty field, an invalid numeric
string, an inappropriate value, or attempting to calculate an average from an
empty list.

### Examples of possible bugs at each stage

| Stage | Possible bug |
|---|---|
| File | Incorrect filename or path; file does not exist |
| Read | File opened in the wrong mode or not closed properly |
| Strings | Program assumes a value is numeric when it is text |
| Clean/validate | Blank lines or missing fields are not detected |
| Convert | `float("hello")` raises `ValueError` |
| Store | A value is appended to the wrong list or wrong position |
| Analyze | Average calculation divides by zero; incorrect formula |
| Report | Output file is overwritten unintentionally or results are formatted unclearly |

---

# Instructor summary

## Concepts demonstrated by each activity

| Activity | Main concepts |
|---|---|
| 1 | `with open`, line-by-line reading, `strip`, `float`, lists, statistics |
| 2 | Writing files, reading output, `"w"` versus `"a"` |
| 3 | `csv.reader`, `next`, row indexes, type conversion, parallel lists |
| 4 | Empty CSV fields, conditional validation, safe conversion |
| 5 | `try` / `except ValueError`, domain validation, `continue` |
| 6 | CSV quoting and embedded newlines, correct record parsing |
| 7 | Numeric conversion, calculations, parallel lists, index matching |
| 8 | File exceptions, conversion exceptions, edge cases, testing |

## Important distinctions to reinforce

1. **A missing value is not the same as zero.** An empty field should not be
   silently converted to `0`.
2. **A convertible value is not necessarily a valid value.** `999.0` is a valid
   float but is outside the experiment's stated acceptable range.
3. **A CSV record is not always one physical line.** Quoted fields can contain
   embedded newlines.
4. **A file error and a conversion error are different.** Handle them where they
   occur, with specific exception types.
5. **Check for an empty list before calculating an average.** Otherwise, the
   program may divide by zero.
6. **Use the CSV module for CSV files.** Splitting every line at commas is not
   reliable when fields can contain commas or embedded line breaks.
