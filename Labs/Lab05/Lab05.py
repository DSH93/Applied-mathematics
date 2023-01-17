#Dor Shukrun 203841697 Lab05 : Exc 1.1 & Exc 2
import sounddevice as sd
import numpy as np
import time


def createSin(sec, fs, freq):
    x = np.arange(0, sec, 1 / fs)
    return np.sin(2 * np.pi * x * freq)


def creatTone(sec, fs, freqs):
    return sum(map(lambda freq: createSin(sec, fs, freq), freqs))


def playTone(sec, fs, freqs):
    tone = creatTone(sec, fs, freqs)
    sd.play(tone)
    time.sleep(sec)


def gramShmidt(inputMat):
    dt = np.float64
    ax = 0
    size = inputMat.shape[0]
    outputMat = np.zeros(np.shape(inputMat), dtype=dt)
    for i in range(size):
        outputMat[:, i] = inputMat[:, i]
        v = inputMat[:, i].reshape(-1, 1)
        for j in range(i):
            u = outputMat[:, j].reshape(-1, 1)
            v = v - ((u.T @ v) / (u.T @ u) * u)
            outputMat[:, i] = v.reshape(-1, )
    gramShmidtOutPut = outputMat / np.linalg.norm(outputMat, axis=ax)
    return gramShmidtOutPut


if __name__ == '__main__':
    playTone(5, 44100, (1209, 697))
    vector = np.array([[1, 2, 3], [-1, 0, -3], [0, -2, 3]])
    print(gramShmidt(vector))
