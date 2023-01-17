import numpy as np


def innerProduc(u, v):
    if (u.size != v.size):
        return False
    return u @ v



if __name__ == "__main__":
    u = np.array([2j, 3, 5, -2, 5], dtype=complex)
    v = np.array([1j, -1j,2, 1, 5], dtype=complex)
    w = np.array([2, 3, -3j, -1, 3], dtype=complex)

    # 1) ================================================
    print("< u , 2v > : ", innerProduc(u, 2 * v), "\n")

    # 2) ================================================
    print("< u , v+2w > : ", innerProduc(u, (v + (2 * w))), "\n")
