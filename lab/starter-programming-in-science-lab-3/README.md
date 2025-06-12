# Programming in Science - Lab 3

This template repository is the starter project for Programming in Science Lab 3. Written in Python, and tested with Pytest.

### Question(s)

1. Write a function that converts polar coordinates (r,θ) to Cartesian coordinates (x,y) using the following formulas. Return the coordinates in a tuple and round the result with 5 decimal points:

Reminder: θ should be converted to radians.

![](Q1_1.png)

![](Q1_2.png)

2. Write a function that converts Cartesian coordinates (x,y) to polar coordinates (r,θ) using the following formulas. Return the coordinates in a tuple and round the result with 5 decimal points:

Reminder: θ should be converted to degrees.

![](Q2_1.png)

![](Q2_2.png)

3. Oscillatory motion is a periodic motion that repeats itself over time, like a pendulum, a vibrating string, or a mass on a spring. In physics, it is often described using the equation: 

Reminder: Phi should be converted to radians.

![](Q3_1.png)

that

![](Q3_2.png)

Where, 

- `x(t)` is the displacement as a function of time,  
- `𝐴` is the amplitude (maximum displacement from equilibrium),  
- `𝜔` is the angular frequency (`𝜔 = 2𝜋𝑓`).  
- `t` is time,  
- `ϕ` is the phase constant, which depends on the initial conditions of the motion.  

### Run Command

`pytest`
