import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import time


def serFunc(Domain, frequency):
    fs = 10000
    Ts = 1 / fs
    f0 = frequency
    t = np.arange(0, Domain, Ts)
    x = np.cos(2 * np.pi * f0 * t)
    sd.play(x, fs)
    plt.plot(t[:100], x[:100])
    plt.grid(axis='both')
    stitle = 'cosine function with freq = ' + str(f0)
    plt.title(stitle)
    plt.show()
    time.sleep(1)


def LadderalSounds():
    for i in range(1, 41):
        serFunc(1, 500 * i)


def ChromaticLadder():
    f0 = 440
    i = 1
    freq = 440
    while (f0 < 20000):
        serFunc(1, freq)
        freq = f0 * i * 2 ** (1 / 12)
        i += 1


if __name__ == '__main__':
    Domain = 1
    frequency = 1000
    # serFunc(Domain, frequency)
    # LadderalSounds()
    ChromaticLadder()