import numpy as np
import matplotlib.pyplot as plt


def innerProduc(u, v):
    if (u.size != v.size):
        return False
    return u @ v


def exc3():
    Ts = 1 / 44100
    x = np.arange(0, 1 - Ts, Ts)
    y1 = np.cos(2 * np.pi * 1 * x)
    plt.plot(x, y1)
    y2 = np.sin(2 * (np.pi * x))
    plt.plot(x, y1, 'b', x, y2, 'r')

    print(innerProduc(y1, y2))
    print(np.vdot(y2,y1))

if __name__ == '__main__':
    exc3()