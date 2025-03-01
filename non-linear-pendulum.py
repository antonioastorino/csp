import time
import numpy as np
import matplotlib.pyplot as plt
import control as ct

# Sate: theta, and omega

animation = True
damping_k = 0.8


def myPlotter(xVals, yVals, xLabel, yLabel, title):
    plt.figure(figsize=(8, 6))
    plt.plot(xVals, yVals, color='blue', linewidth=4)
    plt.title(title)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.grid(visible=True)


def pendulum_update(t, x, u, params):
    theta = x[0]
    omega = x[1]
    torque = u[0]
    damping_k = u[1]
    g = params.get('g')
    l = params.get('l')
    m = params.get('l')
    x_dot = [omega, - g / l * np.sin(theta) + torque / l / l / m - damping_k * omega]
    return x_dot


def pendulum_output(t, x, u, params):
    theta = x[0]
    l = params.get('l')
    return [l * np.sin(theta), - l * np.cos(theta)]


NUM_OF_SAMPLES = 10000
timepts = np.linspace(0, 10, NUM_OF_SAMPLES + 1)
params = {'g': 9.8, 'l': .5, 'm': .5}
u = [[0 for _ in range(0, NUM_OF_SAMPLES + 1)] for _ in range(0, 2)]
u[0][0:4000] = [
    2 *
    np.sin(
        np.sqrt(params.get('g') / params.get('l')) * timepts[i]) for i in range(
        0,
        4000)]
u[1] = [damping_k for _ in range(0, NUM_OF_SAMPLES + 1)]

myPlotter(timepts, u[0], 't', 'input', "Input torque")

pendulum = ct.NonlinearIOSystem(
    pendulum_update,
    pendulum_output,
    states=2,
    name='pendulum',
    inputs=['f', 'dumping coefficient'],
    outputs=['x', 'y'],
    params=params)

start_time = time.time()
t_vec, out_vec = ct.input_output_response(pendulum, timepts, u, 0)
print("Computation time: ", time.time() - start_time)

myPlotter(t_vec, out_vec[0], 't', 'x', 'x vs time')
if (animation):
    l = params.get('l')
    fig, ax = plt.subplots()
    ax.set_xlim(-l * 1.1, l * 1.1)
    ax.set_ylim(-l * 1.1, l * 1.1)
    ax.set_aspect('equal', adjustable='box')
    position_plot, = ax.plot(0, 0, marker='*')
    refresh_rate = 50  # Hz
    dt = 1 / refresh_rate  # s
    sampling_time = 0
    for i in range(0, NUM_OF_SAMPLES + 1):
        if t_vec[i] > sampling_time:
            position_plot.set_data([0, out_vec[0][i]], [0, out_vec[1][i]])
            plt.pause(dt)
            sampling_time += dt
plt.show()
