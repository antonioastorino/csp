'''
Attempt to implement a non-linear pendulum using:
theta_double_dot = - g / l * sin (theta)

NOTE: I cannot find a better implementation online so I made this up and I am not sure it's correct.

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

The problem is setting the initial conditions. Basically, you can define it in terms of initial
displacement (theta(t = -dt) and theta(t = 0)). This is undesirable because if you change the
time interval `dt`, the same displacement would occur within a different time slot. So, don't
change `dt` or try to also change the initial delta `theta` accordingly.

> NOTE: python is slow at rendering and your frame rate is anyway the bottleneck. For this reason,
    the `dt` used for generating data is not the same used to update the animation
'''

import numpy as np
import matplotlib.pyplot as plt

DURATION = 10  # s
dt = 0.001  # s
G = 9.81  # m / s^2
L = 2  # m

NUM_OF_SAMPLES = round(DURATION / dt)

def myPlotter(xVals, yVals, xLabel, yLabel, title):
    plt.figure(figsize=(8, 6))
    plt.plot(xVals, yVals, color='blue', linewidth=4)
    plt.title(title)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.grid(visible=True)


def theta_t_plus_dt(dt, theta_t, theta_t_minus_dt):
    return -G / L * np.sin(theta_t) * (dt * dt) - theta_t_minus_dt + 2 * theta_t


t = np.linspace(0, NUM_OF_SAMPLES * dt, NUM_OF_SAMPLES - 1)
theta_curr = np.pi / 730
theta_prev = 0
theta_next = 0
theta_saved = []
for i in range(0, NUM_OF_SAMPLES - 1):
    theta_next = theta_t_plus_dt(dt, theta_curr, theta_prev)
    theta_prev = theta_curr
    theta_curr = theta_next
    theta_saved.append(theta_curr)

myPlotter(t, theta_saved, 't [s]', 'theta [rad]', 'time vs angle')

fig, ax = plt.subplots()
ax.set_xlim(-L * 1.1, L * 1.1)
ax.set_ylim(-L * 1.1, L * 1.1)
ax.set_aspect('equal', adjustable='box')
position_plot, = ax.plot(1, 1, marker='*')
refresh_rate = 50  # Hz
undersampling_rate = round(1 / dt / refresh_rate)
for i in range(0, NUM_OF_SAMPLES - 1, undersampling_rate):
    position_plot.set_data([0, L * np.sin(theta_saved[i])], [0, - L * np.cos(theta_saved[i])])
    plt.pause(1 / refresh_rate)
plt.show()
