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



if __name__ == '__main__':
    playTone(5, 44100, (1209, 697))
