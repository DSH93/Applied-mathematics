import numpy as np
import matplotlib.pyplot as plt
import math


def a():
    X = np.zeros([8, 8])
    X[1, 1:3] = 1
    X[1, 5:7] = 1
    X[3, 3:5] = 1
    X[5:7, 1::5] = 1
    X[6, 2:6] = 1
    plt.imshow(X, cmap='gray')
    plt.show()


def b():
    X = np.ones([8, 8])
    X[1, 1:3] = 0
    X[1, 5:7] = 0
    X[3, 3:5] = 0
    X[5:7, 1::5] = 0
    X[6, 2:6] = 0
    plt.imshow(X, cmap='gray')
    plt.show()


def c(matrixA, matrixB):
    normMatrixA = math.sqrt((matrixA @ matrixA.transpose()).trace())
    normMatrixB = math.sqrt((matrixB @ matrixB.transpose()).trace())
    normMatrixAB = normMatrixA * normMatrixB
    frobeniusInnerProduct = (matrixA.transpose() @ matrixB).trace()
    normalFrobenius = frobeniusInnerProduct / normMatrixAB
    return normalFrobenius >= 0.7


def fake():
    x = np.zeros([8, 8])
    for i in range(1, 7):
        for j in range(1, 7):
            x[i][j] = np.random.randint(0, 2)
    return x

def d():
    y = mat()
    while (True):
        #
        x = fake()
        if (c(x, y)):
            print("Access Permitted")
            plt.imshow(y, cmap='gray')
            plt.show()
            plt.imshow(x, cmap='gray')
            plt.show()
            break;

        else:
            print("Access Denied")


def mat():
    X = np.zeros([8, 8])
    X[1, 1:3] = 1
    X[1, 5:7] = 1
    X[3, 3:5] = 1
    X[5:7, 1::5] = 1
    X[6, 2:6] = 1
    return X


if __name__ == '__main__':
    # a()
    # b()
    # v = mat()
    # u = mat()
    # c(u, v)
    d()
