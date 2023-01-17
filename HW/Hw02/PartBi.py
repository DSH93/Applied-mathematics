import numpy as np


def normip(v, p):
    """
    function to compute the natural norm of an input vector.
    Inputs: v - a numpy array (n dim vector)
    Outputs: natural norm of v
    """
    norm = 0
    for i in range(v.size):
        norm += (v[i] ** p)
    return norm ** (1 / p)


def normalVectorByNorm(v, p):
    norm = normip(v, p)
    for i in range(v.size):
        v[i] /= norm
    return v


def distance(v, u, p):
    vu = v.copy()
    for i in range(v.size):
        vu[i] = (u[i] - v[i])
    result = normip(vu, p)
    return result


if __name__ == '__main__':
    # 1
    v = np.array([1, 2j, -3, 1, 7], dtype=complex)
    p = 2
    print("Exc 1: \nThe Norm of v:\n", normip(v, p), "\n")
    # 2.a
    v = np.array([1, 5, 3j, -1 + 1j, 2], dtype=complex)
    print("Exc 2.a: \nThe Normal dir Vector:\n", normalVectorByNorm(v, p), "\n")
    # 2.b
    v = np.array([6, 7, 1j, 2j, 7], dtype=complex)
    u = np.array([2, 1, -2j, -3, 8], dtype=complex)
    print("Exc 2.b: \nThe Distance Between the Vectors is: \n", distance(v, u, p))
