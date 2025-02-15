import matplotlib.pyplot as plt
import numpy as np

g = 9.81
v0 = 5
h = 100


def tray(x):
    return (-g / {2 * v0**2}) * x**2 + h


x = np.linspace(0, 2 * v0**2 / g, 100)
y = tray(x)

plt.plot(x, y)
