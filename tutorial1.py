'''
Resources:
- Python Control Systems Library Tutorial 1: https://www.youtube.com/watch?v=ZNBAq9dT4IE
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
    plt.show()

'''
example:
     2 s + 1
 ---------------
 3 s^2 + 2 s + 1
'''

num = [2, 1]
den = [3, 2, 1]
W = ct.tf(num, den)
print(W)
tVec = np.linspace(0, 50, 10000)
t, y = ct.step_response(W, tVec)
myPlotter(t, y, 't', 'y', 'W - step response')

