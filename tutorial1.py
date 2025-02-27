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

xVals = [1, 2]
yVals = [3, 2]
myPlotter(xVals, yVals, 'x', 'y', 'hello')

