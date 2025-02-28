'''
Attempt to implement a non-linear pendulum with input force using:

    theta_double_dot = - g / l * sin (theta) + input_torque / l / m / l

where
            1 / l        1 / m               1 / l
    torque  -----> force -----> acceleration -----> angular_acceleration

This scripts generates and plots the behavior of `theta` with respect to time and a rudimental
animation of the pendulum.

> NOTE: I cannot find a better implementation online so I made this up and I am not sure this is
        correct.

The update equation follows this idea. I don't know a closed formula for the speed (theta_dot).
Therefore, I create two functions where the speed has opposite sign and add them up:
theta(t + dt) - theta(t) ~ +theta_dot(t) * dt + 1/2 theta_double_dot(t) * dt^2  +
theta(t - dt) - theta(t) ~ -theta_dot(t) * dt + 1/2 theta_double_dot(t) * dt^2  =
--------------------------------------------------------------------------------
theta(t + dt) + theta(t - dt) ~ theta_double_dot(t) * dt^2
=>
theta(t + dt) ~ theta_double_dot(t) * dt^2 - theta(t - dt)
=>
theta(t + dt) ~ -g / l * sin (theta) * dt^2 - theta(t - dt)

The initial condition can be assigned by setting:
- `INITIAL_DELTA_THETA != 0` (not recommended - see `non-linear-pendulum.py`)
- `forced_torque_vec` as a vector of torque applied for the first N time steps

'''

import numpy as np
import matplotlib.pyplot as plt

######################################## Parameters ###############################################
animation = True
INITIAL_DELTA_THETA = 0
DURATION = 6  # s
l = 1  # m
m = 0.5  # kg
forced_torque_vec = [- 0.5 for _ in range(0, 1000)]
#################################### End of parameters ############################################

dt = 0.001  # s
g = 9.81  # m / s^2
NUM_OF_SAMPLES = round(DURATION / dt)


def myPlotter(xVals, yVals, xLabel, yLabel, title):
    plt.figure(figsize=(8, 6))
    plt.plot(xVals, yVals, color='blue', linewidth=4)
    plt.title(title)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.grid(visible=True)


def theta_t_plus_dt(dt, theta_t, theta_t_minus_dt, forced_torque=0):
    alpha = -g / l * np.sin(theta_t) + forced_torque / m / (l * l)
    return alpha * (dt * dt) - theta_t_minus_dt + 2 * theta_t


t = np.linspace(0, NUM_OF_SAMPLES * dt, NUM_OF_SAMPLES - 1)
theta_curr = INITIAL_DELTA_THETA
theta_prev = 0
theta_next = 0
theta_vec = [0 for _ in range(1, NUM_OF_SAMPLES)]
omega_vec = [0 for _ in range(1, NUM_OF_SAMPLES)]
torque_vec = [0 for _ in range(1, NUM_OF_SAMPLES)]
len_of_forced_torque_vec = min(NUM_OF_SAMPLES - 1, len(forced_torque_vec))

# If there is any user-defined torque, this will be used as a system input
for i in range(0, len_of_forced_torque_vec):
    torque_vec[i] = forced_torque_vec[i]

for i in range(0, NUM_OF_SAMPLES - 1):
    theta_next = theta_t_plus_dt(dt, theta_curr, theta_prev, torque_vec[i])
    omega_vec[i] = (theta_next - theta_curr) / dt
    theta_prev = theta_curr
    theta_curr = theta_next
    theta_vec[i] = theta_curr

myPlotter(t, theta_vec, 't [s]', 'theta [rad]', 'time vs angle')

# Energy / state space
myPlotter(theta_vec, omega_vec, 'theta', 'omega', 'State Space')
KE = [(omega_vec[i] * l)**2 * m / 2 for i in range(0, NUM_OF_SAMPLES - 1)]
U = [m * g * l * (1 - np.cos(theta_vec[i])) for i in range(0, NUM_OF_SAMPLES - 1)]
E = [KE[i] + U[i] for i in range(0, NUM_OF_SAMPLES - 1)]
myPlotter(KE, U, 'kinetic [J]', 'potential [J]', 'Energy')
myPlotter(t, E, 'time [s]', 'total energy [J]', 'Energy vs time')

if (animation):
    fig, ax = plt.subplots()
    ax.set_xlim(-l * 1.1, l * 1.1)
    ax.set_ylim(-l * 1.1, l * 1.1)
    ax.set_aspect('equal', adjustable='box')
    position_plot, = ax.plot(0, 0, marker='*')
    refresh_rate = 50  # Hz
    undersampling_rate = round(1 / dt / refresh_rate)
    for i in range(0, NUM_OF_SAMPLES - 1, undersampling_rate):
        position_plot.set_data([0, l * np.sin(theta_vec[i])], [0, - l * np.cos(theta_vec[i])])
        plt.pause(1 / refresh_rate)

plt.show()
