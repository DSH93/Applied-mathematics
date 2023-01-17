#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import scipy
import math

import matplotlib

matplotlib.use('TkAgg')


def fourier_series(ax, func, order, x_resolution):
    an = np.zeros(order)
    bn = np.zeros(order)
    app = np.zeros(x_resolution)
    xAxis = np.linspace(-np.pi, np.pi, x_resolution)

    n = 0
    fan = lambda x: func(x) * np.cos(x * n) * (1 / np.pi)
    fbn = lambda x: func(x) * np.sin(x * n) * (1 / np.pi)
    an[0] = (scipy.integrate.quad(fan, -np.pi, np.pi)[0])
    bn[0] = 0
    for n in range(1, order):
        an[n] = (scipy.integrate.quad(fan, -np.pi, np.pi)[0])
        bn[n] = (scipy.integrate.quad(fbn, -np.pi, np.pi)[0])

    for n in range(1, order):
        app += an[n] * np.cos(n * xAxis) + bn[n] * np.sin(n * xAxis)
    app += (an[0] / 2)

    ax.plot(xAxis, func(xAxis), linestyle=(0, (1, 1)), color='red', label='fx')
    ax.plot(xAxis, app, linestyle=(5, (10, 3)), color='blue', label='fx app')
    ax.legend()

    return an, bn


def rectangular_rule_integration(func, left, right, n_rects):
    f = eval(func)
    h = (right - left) / n_rects
    y = h * np.sum(f[:-1])
    return y


def run(figure):
    width = 3
    functions = ((11, lambda x: x ** 2, 'x^2'),
                 (2, np.cos, 'cos(x)'),
                 (7, lambda x: x, 'x'),
                 (3, lambda x: x ** 3, 'x^3'),
                 (3, np.sin, 'sin(x)'),
                 (4, lambda x: x + 3 + x ** 2, 'x+3+x^2'))
    fig, ax = plt.subplots(math.ceil(len(functions) / width), width)
    for i, of in enumerate(functions):
        axi = ax[i // width, i % width]

        fourier_series(axi, of[1], of[0], 10000)
        axi.set_title(of[2])
    if figure is None:
        fig.show()
    else:
        fig.savefig(figure)


if __name__ == '__main__':
    run('pic')
