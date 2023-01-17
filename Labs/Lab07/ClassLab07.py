import matplotlib

matplotlib.use('TkAgg')

import numpy as np
import matplotlib.pyplot as plt


def cisTheta(r):
    x = np.linspace(0, 1, 10000)
    theta = r * (np.cos(2 * np.pi * x) + 1j * np.sin(2 * np.pi * x))
    fig, ax = plt.subplots()
    ax.plot(x, theta.real)
    ax.plot(x, theta.imag)
    ax.legend(['real', 'imag'])
    ax.set_title('cis(theta)')
    fig.show()
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.plot(theta, np.ones(theta.shape) * r)
    fig.show()


r = 1
cisTheta(r)