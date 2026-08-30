# Programming in Science — Lab 1
## Python Foundations: Predict, Code, Test, Debug

**Estimated time:** 70–90 minutes  
**Starter:** `starter-programming-in-science-lab-1`  


## Learning objectives

You will practice:

- Python statements and variables;
- data types and input conversion;
- reading tests before coding;
- predicting behavior before running;
- debugging;
- satisfying automated tests;
- explaining your code.

## Part 0 — Read Before Coding

Open `Lab1.py` and use the examples in this handout for manual testing.

Answer:

1. What two functions must you implement?
2. What evidence in the test tells you exactly what `hello_world()` must print?
3. What three values does `input_output()` read?
4. Why does the test use `StringIO`?
5. Why should you not modify the test file?

## Part 1 — Hello World

Implement:

```python
def hello_world():
```

Required output:

```text
Hello, World!
```

### Predict

If the function contains only `pass`, will the test pass? Explain before running it.

Then run:

```text
Run the program and compare its output with your predicted results.
```

## Part 2 — Input and Output

Implement:

```python
def input_output():
```

Read:

1. name as `str`;
2. age as `int`;
3. height as `float`.

Example:

```text
Enter your name: Alice
Enter your age: 25
Enter your height: 5.7
Hello, Alice!
You are 25 years old.
Your height is 5.7 meters.
```

### Think first

What type would `age` have if you wrote:

```python
age = input("Enter your age: ")
```

Why is this different?

```python
age = int(input("Enter your age: "))
```

## Part 3 — Test-Driven Reading

The supplied test simulates input:

```python
user_inputs = ["Alice", "25", "5.7"]
```

It then captures the output and compares it with the expected result.

### Mini challenge

Predict which of the following would make the test fail:

```python
print("Hello, Alice!")
print("You are 25 years old.")
print("Your height is 5.7 meters.")
```

What if you print:

```python
print("Hello, Alice")
```

instead?

Explain why exact output can matter in automated testing.

## Part 4 — Debugging Detective

Consider:

```python
age = input("Enter age: ")
print(age + 5)
```

### Questions

1. What type is `age`?
2. What error do you expect?
3. How would you correct it?
4. Why is this a type problem rather than an arithmetic problem?

Now test your explanation in Python.

## Part 5 — Small Modification Challenge

After your required functions pass, make a temporary copy of your solution and modify the program so that it also displays:

```text
In five years, you will be 30 years old.
```

Do not change the required function signature or the supplied test file.

Explain why this modification can be made without changing the original input type.

## Part 6 — Responsible AI Check

If you use an AI assistant, ask it to explain **one** error or design decision rather than asking it to write the entire lab.

Then:

1. compare its explanation with your own reasoning;
2. test the suggestion;
3. identify whether you accepted or rejected it;
4. write one sentence explaining why.

You are responsible for every line you submit.

## Submission checklist

- [ ] `hello_world()` implemented
- [ ] `input_output()` implemented
- [ ] Manual tests and edge cases pass
- [ ] Part 0 questions answered
- [ ] debugging challenge answered and tested
- [ ] modification challenge attempted
- [ ] AI reflection completed if AI was used

## Suggested grading

| Component | Marks |
|---|---:|
| Pre-coding analysis | 10 |
| `hello_world()` | 10 |
| `input_output()` | 20 |
| Test/code reasoning | 10 |
| Debugging | 15 |
| Modification challenge | 15 |
| Explanation/AI reflection | 10 |
| **Total** | **90** |
