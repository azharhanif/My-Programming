# Programming in Science - Lab 8
## Oscillatory and Standing Wave Data Challenge

read oscillatory wave CSV data, compute mean/max amplitude, and read standing wave data to compute wave speed from 
```
v = \sqrt{T/μ} with μ=1.
```

### Question(s) 
You are a lab assistant analyzing two wave datasets.
### Scenario 
Each student must compute these three personalization values from their student ID before starting:
```
•	d1 = last digit of student ID

•	d2 = second-last digit of student ID

•	k = (d1 + d2) % 4 + 2

•	shift = d1 - d2

•	rows_keep = (d1 % 2) + 2

Students must include these values at the top of every submission and use them in their code. 

This forces outputs to differ across students.
```
#### Component A: Build from the lecture 9 examples (50 marks)
```
Write two functions:

•	read_oscillatory_wave_data(filename)

•	read_standing_wave_data(filename)
 
```
The first must:
```
read a CSV with length and amplitude,

compute and print mean amplitude and maximum amplitude.
```
The second must:
```
read a CSV with length and tension,

compute wave speed using:
`v = sqrt(T / 1)`.
```
#### Component B — ID-based modification (50 marks)
Create personalized versions of both input files:
##### Oscillatory file
• create `5 + d2` rows,

• add `shift` to all amplitude values,

• compute the new mean and max.

##### Standing wave file
• create `4 + rows_keep` rows,

• multiply every tension value by `k`,

• compute the new wave speeds

✅ **Required details** 
```
•	Filenames must include the student ID.

•   Data values must be different across students because row counts and arithmetic are ID-based.


```
### Run Command

`pytest`
