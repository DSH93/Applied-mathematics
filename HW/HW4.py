import matplotlib.pyplot as plt
import numpy as np


def FourierSynthesis(cn, func, m, N):
    x = np.linspace(-np.pi, np.pi, N)
    fu = eval(func)
    Sm = 0
    ShowFourierSynthesis(cn, fu, m, x, Sm)
    for n in range(-m, m + 1):
        Sm += eval(cn) * np.exp(1j * x * n)
    return Sm


def ShowFourierSynthesis(cn, fu, m, x, Sm):
    for n in range(-m, m + 1):
        Sm += eval(cn) * np.exp(1j * x * n)
        plt.plot(x, Sm)
        plt.plot(x, fu)
        plt.show()


if __name__ == '__main__':
    # A  B.1  B.2  C
    cn1 = '((((-1)**n) * (np.exp(np.pi) - np.exp(-np.pi))) / (2 * np.pi * (1 - 1j * n)))'
    cn2 = '(-((-1)**n)/1j*n)'
    f1 = 'np.exp(x)'
    f2 = 'x'
    FourierSynthesis(cn1, f1, 30, 20)
