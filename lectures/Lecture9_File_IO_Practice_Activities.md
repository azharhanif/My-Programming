# Lecture 9: File I/O — Practice Activities

These activities extend the examples in Lecture 9. They use the same tools and ideas:
`open()`, `with`, `read()`, line-by-line reading, `strip()`, writing, `csv.reader()`,
type conversion, lists, validation, and exception handling.

## Before you begin: project setup

Create a project folder named `Lecture9`. Inside it, create a Python file named
`file_io_practice.py` and a folder named `data`. Download the supplied sample files
and place them inside `data`.

Your folder should look like this:

```text
Lecture9/
├── file_io_practice.py
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

Run your program from the `Lecture9` folder so paths such as
`data/temperatures.txt` work as written.

**Important:** CSV values are strings when read. Convert numeric fields before
performing arithmetic. These activities use lists and column indexes; they do not
require dictionaries.

---

## Activity 1 — Read, clean, and convert text data

**Files:** `temperatures.txt`, then `numbers_with_spaces.txt`

The first file contains one temperature per line.

1. Open `data/temperatures.txt` using `with open(...)`.
2. Read the file line by line.
3. Remove the newline using `strip()`.
4. Convert each value to `float`.
5. Store the values in a list named `temperatures`.
6. Display the list, number of readings, minimum, maximum, and average.

**Check your result:** There should be 5 readings. The minimum is 19.8 and the
maximum is 22.4.

**Extension:** Repeat using `numbers_with_spaces.txt`. This file includes blank
lines and extra spaces. Skip blank lines after calling `strip()`; do not attempt
to convert an empty string to `float`.

Questions:
- Why is `strip()` needed before conversion?
- Why should the blank line be skipped?
- What is the difference between a string such as `"20.5"` and the float `20.5`?

## Activity 2 — Write a report to a file

**Input:** Use the list from Activity 1.

1. Calculate the number of readings, minimum, maximum, and average.
2. Open `temperature_report.txt` in write mode (`"w"`).
3. Write a short report containing those results.
4. Open the same file in read mode and display its contents.

**Extension:** Run the program a second time after adding a sentence manually to
the report. Observe what happens when you use `"w"`. Change the mode to `"a"` and
run it again. Explain the difference between overwrite and append.

Do not submit a screenshot only: make sure your program creates the report file.

## Activity 3 — Read a CSV file and calculate class results

**File:** `student_scores.csv`

The first row is a header. The remaining rows contain student ID, name, program,
and score.

1. Import `csv`.
2. Open the file using `newline=""`.
3. Create a `csv.reader`.
4. Skip the header using `next(reader)`.
5. For each row, read the name from `row[1]` and score text from `row[3]`.
6. Convert the score to `float` and store scores in a list.
7. Calculate and display the class average, highest score, and lowest score.

**Extension:** Also display the name of the student with the highest score.
You may keep a separate list of names aligned by index with the scores list.

Questions:
- Why does `csv.reader()` return strings?
- Why do we call `next(reader)`?
- What does `row[3]` refer to?

## Activity 4 — Detect missing CSV values

**File:** `student_scores_missing.csv`

This file contains two incomplete records: one missing score and one missing
program.

1. Read the CSV file and skip its header.
2. For each row, inspect the program field (`row[2]`) and score field (`row[3]`).
3. If either field is `""`, print a message identifying the student and the
   missing information.
4. Only convert a score to `float` when the score field is not empty.
5. Count how many complete score values are available and calculate their average.

**Important:** An empty CSV field is read as an empty string (`""`). It is not
automatically converted to `None` or `0`.

**Extension:** Print two separate counts: number of missing programs and number
of missing scores.

## Activity 5 — Validate measurements before calculating

**File:** `messy_measurements.csv`

The file contains valid measurements, a missing value, text in a numeric column,
and an implausible value. Assume the experiment measures a small object whose
mass must be between 0 and 20 grams.

1. Read the CSV file and skip the header.
2. For each row, obtain the sample ID (`row[0]`) and mass text (`row[1]`).
3. If the mass text is empty, report a missing value.
4. Otherwise, use `try`/`except ValueError` when converting it to `float`.
5. If conversion succeeds, accept only values greater than 0 and less than or
   equal to 20.
6. Store accepted masses in a list.
7. Display the accepted values and their average.

Your program should not crash because of `not_available` or the blank field.

Questions:
- Which problem is detected by checking for `""`?
- Which problem is detected by `except ValueError`?
- Why is `999.0` not a conversion error, even though it is not acceptable here?
- Why must the acceptable range come from knowledge of the experiment?

## Activity 6 — CSV records with a line break inside a field

**File:** `comments_multiline.csv`

One comment contains a line break inside quotation marks. It is still one CSV
record.

1. Read the file using `csv.reader()` and `newline=""`.
2. Skip the header.
3. Print each student's ID, name, and complete comment.
4. Count the number of student records.

**Check your result:** There are 3 student records, not 4. The first student's
comment spans two physical lines but belongs to one CSV record.

Question: Why is it safer to let `csv.reader()` identify records than to split
the file manually at every newline?

## Activity 7 — Create an inventory summary

**File:** `inventory.csv`

Columns: item, quantity, unit price.

1. Read the file using `csv.reader()` and skip the header.
2. Convert quantity to `int` and unit price to `float`.
3. Calculate each item's inventory value (`quantity * unit_price`).
4. Display each item and its inventory value.
5. Calculate the total inventory value.

**Check your result:** The total inventory value is 78.15.

**Extension:** Find the item with the greatest inventory value. Keep the item
names and calculated values in parallel lists and use the same index to connect
them.

## Activity 8 — File I/O testing challenge

Write a program that reads a filename supplied in a variable and processes one
numeric value per line. Test it with the supplied files and with your own small
test files.

Your program should handle these cases deliberately:

- a normal file;
- an empty file;
- a file containing only blank lines;
- a malformed numeric value;
- a missing file;
- a file containing one valid value.

For each case, decide what the program should report. Use `try`/`except` for
file-opening and numeric-conversion errors. Do not hide errors with a broad
`except:` clause.

### Final reflection

In 3–5 sentences, explain the full file-processing pipeline:

```text
file → read → strings → clean/validate → convert → store → analyze → report
```

Give one example of a bug that can occur at each of these stages.
