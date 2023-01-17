from functools import partial
import numpy as np

from functools import partial


# m = np.array(range(9)).reshape((3, 3))
# np.roll(m, 1, axis=0)


def e(n):
    s = 0
    while n > 0:
        n -= 1
        s += 1
        yield s
    return None


def fib(n):
    a = 0
    b = 1
    for _ in range(n):
        yield b
        a, b = b, a + b
    return None


def plotfib(fi, ax, matrix_d):
    matrix = matrix_d['m']
    matrix = np.roll(matrix, (fi, fi), axis=(0, 1))


if __name__ == '__main__':
    for i in fib(10):
        print(i)

    partial(lambda x, y:, partial)
