'''
Resources:
- Python Control Systems Library Tutorial 2: https://www.youtube.com/watch?v=qBDcHKkHzIE&t
'''
import matplotlib.pyplot as plt
import control as ct
import numpy as np


def myPlotter(xVals, yVals, xLabel, yLabel, title):
    plt.figure(figsize=(8, 6))
    plt.plot(xVals, yVals, color='blue', linewidth=4)
    plt.title(title)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.grid(visible=True)

A = np.array([[-2, 1], [-1, 0]])
B = np.array([[1], [0]])
C = np.array([[1, -2]])
D = np.array([[0]])
#
sys = ct.ss(A, B, C, D)
print(sys)
w = ct.ss2tf(sys)
print("Transfer function")
print(w)

ct.damp(sys, doprint=True)
ct.poles(sys)
ct.zeros(sys)
print("poles and zeros")
ct.pzmap(sys)
print("SISO tool")
plt.figure(figsize=(8, 6))
ct.sisotool(sys)
sys = ct.tf2ss(w)
print(sys)
plt.show()

