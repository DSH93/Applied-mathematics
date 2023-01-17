from typing import Iterable, Set
import numpy as np


def innerProd(c1: Iterable[complex], c2: Iterable[complex]):
    return sum(map((lambda a: a[0] * a[1].conjugate()), zip(c1, c2)))


if __name__ == '__main__':
    a = complex(1, 5)
    b = complex(2, 5)
    c = complex(3, 5)
    d = complex(5, 1)
    e = complex(4, 2)

    c1 = [a, b, c, d]
    c2 = [b, c, d, e]
    print("innerProd: ", innerProd(c1, c2))
    print("vdot:      ", np.vdot(c2, c1))
