#!/usr/bin/env python3

import math
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple, Optional

matplotlib.use('TkAgg')


# def cisTheta(r):
#     x = np.linspace(0, 1, 10000)
#     theta = r * (np.cos(2 * np.pi * x) + 1j * np.sin(2 * np.pi * x))
#     fig, ax = plt.subplots()
#     ax.plot(x, theta.real)
#     ax.plot(x, theta.imag)
#     ax.legend(['real', 'imag'])
#     ax.set_title('cis(theta)')
#     fig.show()
#     fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
#     ax.plot(theta, np.ones(theta.shape) * r)


def polar(z: complex) -> Tuple[float, float]:
    x = float(z.real)
    y = float(z.imag)
    theta = math.tan(y / x)
    r = float(abs(z))
    return r, theta


def get_roots(z: complex, n: int) -> np.ndarray:
    roots = np.zeros((n,), dtype=np.complex64)
    r, theta = polar(z)
    for k in range(n):
        zk = (r ** (1 / n)) * (np.cos((theta + 2 * np.pi * k) / n) + 1j * np.sin((theta + 2 * np.pi * k) / n))
        roots[k] = zk

    return roots

def plot_roots(z: complex, n: int):
    x = []
    y = []
    roots = get_roots(z, n)
    for complexNumber in range(roots.size):
        x.append(roots[complexNumber].real)
        y.append(roots[complexNumber].imag)

    x.append(roots[0].real)
    y.append(roots[0].imag)
    plt.plot(x, y)

def run(z: complex, n: int, figure: Optional[str]):
    plt.close()
    plot_roots(z, n)
    if figure is None:
        plt.show()
    else:
        plt.savefig(figure)

if __name__ == '__main__':
    run(z=3 + 2j, n=8, figure='fig.png')
