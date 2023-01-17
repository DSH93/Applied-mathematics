import numpy as np


def gramShmidt(A):
    A = A.T
    eps = 1e-14
    n = A.shape[1]
    Q = np.zeros(np.shape(A), dtype=np.float64)
    R = np.zeros((n, n), dtype=np.float64)
    for j in range(n):
        v = A[:, j].reshape(-1, 1)
        for i in range(j):
            R[i, j] = Q[:, i].reshape(-1, 1).T @ v
            v = v - R[i, j] * Q[:, i].reshape(-1, 1)
        if (sum(v * v)) <= eps:
            A = np.delete(A, j, axis=1)
            continue
        v = v.reshape((-1,))
        R[j, j] = np.linalg.norm(v)
        Q[:, j] = v / R[j, j]
    return [A, Q, R]


if __name__ == '__main__':
    a = np.array([[1, 2, 3, 2, 1], [1, 1, -1, 1, 0], [3, 4, 1, 4, 1]])
    AQRlst = gramShmidt(a)
    for mat in AQRlst:
        print(str(mat) + " \n")
