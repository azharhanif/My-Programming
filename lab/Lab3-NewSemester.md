# Programming in Science — Lab 3
## Coordinate Systems and Oscillatory Motion

**Estimated time:** 75–90 minutes  
**Core skill:** translating scientific formulas into functions, handling units, and validating results.

### Learning objectives
You will practice:
- identifying inputs and outputs from a scientific formula;
- converting degrees/radians correctly;
- writing small reusable functions;
- rounding only at the presentation stage;
- checking results against simple known cases;
- debugging a scientifically plausible but incorrect program.

---

## Part A — Polar → Cartesian

Use

\[
x=r\cos(\theta), \qquad y=r\sin(\theta)
\]

where the input angle is in **degrees**.

Write:

```python
def polar_to_cartesian(r, theta_degrees):
    ...
```

Return `(x, y)`, rounded to 5 decimal places.

### Before coding
Predict the result for:

```text
r = 1, theta = 0
r = 1, theta = 90
r = 2, theta = 180
```

What should happen at 0° and 90°? Explain.

### Implementation requirement
Convert the angle to radians before calling `sin()` or `cos()`.

---

## Part B — Cartesian → Polar

Use:

\[
r=\sqrt{x^2+y^2}
\]

and an appropriate inverse tangent function for the angle.

Write:

```python
def cartesian_to_polar(x, y):
    ...
```

Return `(r, theta_degrees)`, rounded to 5 decimal places.

### Important reasoning
Why is `atan2(y, x)` safer than simply using `atan(y/x)`?

Test points from all four quadrants.

---

## Part C — Round-trip test

Choose several points:

```text
(1, 0)
(0, 1)
(-1, 0)
(1, 1)
(-2, 3)
```

Convert Cartesian → polar → Cartesian.

Do not expect floating-point results to be perfectly identical. Explain why rounding is useful here.

---

## Part D — Oscillatory Motion

Use:

\[
x(t)=A\cos(\omega t+\phi)
\]

with:

\[
\omega=2\pi f
\]

Write:

```python
def oscillation(A, f, t, phi_degrees):
    ...
```

Convert `phi` to radians.

### Predict first
For:

```text
A = 2
f = 1
phi = 0
```

What should `x(0)` be? What should happen at `t = 0.5`?

---

## Part E — Debugging challenge

A student wrote:

```python
def oscillation(A, f, t, phi):
    omega = 2 * math.pi * f
    return A * math.cos(omega * t + phi)
```

The student says:

> "My formula is correct, so I don't need to convert phi."

What is wrong with this reasoning if `phi` is supplied in degrees?

Give a counterexample.

---

## Part F — Explain before you leave

Answer briefly:

1. Why do scientific programs need unit awareness?
2. Why is `atan2()` preferable for Cartesian → polar?
3. Why should rounding normally happen after the calculation?
4. Give one test case that could expose an angle-conversion bug.

### Submission
Submit your `.py` file and your written reasoning in comments.
