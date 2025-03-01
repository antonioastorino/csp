# Control Systems in Python
Learning how to use the Control Systems Python library

## Examples
### Linear system 1
Self explanatory...
```bash
python3 tutorial1.py
```
### Linear system 2
Also self explanatory...
```bash
python3 tutorial2.py
```

### Non-linear pendulum
Usint the `NonlinearIOSystem` class
```bash
python3 non-linear-pendulum.py
```
The system state $`x`$ is described by

```math
\begin{bmatrix}
x_0 \\
x_1
\end{bmatrix}
=
\begin{bmatrix}
\theta\\
\omega
\end{bmatrix}
```

and its time evolution is 

```math
\begin{bmatrix}
\dot{x}_0 \\
\dot{x}_1
\end{bmatrix} =
\begin{bmatrix}
\omega \\
\alpha
\end{bmatrix}
=
\begin{bmatrix}
x_1\\
- \dfrac{g}{l} \sin(\theta) + \dfrac{\tau_{in}}{l^2 m} - k\omega
\end{bmatrix}
```

where
- $`\theta`$ is the angular position
- $`\omega`$ the angular velocity
- $`\alpha`$ is the angular acceleration
- $`\tau_{in}`$ is the applied torque
- $`k`$ is the damping coefficient

This method works ok.
I solved the same problem using [my own method](https://github.com/antonioastorino/nlp) and found out that **mine is about 10 times faster** than `NonlinearIOSystem`.
The computation time is printed by both examples.

# Resources:
- [YouTube Tutorial 1](https://www.youtube.com/watch?v=ZNBAq9dT4IE)
- [YouTube Tutorial 2](https://www.youtube.com/watch?v=qBDcHKkHzIE&t)
- [Library documentation](https://python-control.readthedocs.io/en/0.10.1/)
- [Python Control Library Example](https://www.cds.caltech.edu/~murray/courses/cds112/wi2023/W1_python-control.pdf)
- [Non-linear Pendulum GitHub](https://github.com/antonioastorino/nlp)
