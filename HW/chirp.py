import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt


def chirp(f0, u, fs, dur):
### A ####
    tt = np.linspace(0, dur, int(fs * dur))
    sig = np.cos(2 * np.pi * f0 * tt + 2 * np.pi * u * tt ** 2)
    return sig, tt




if __name__ == '__main__':
    f0 = 1000
    u = 550
    fs = 44100
    dur = 15
    tsig = 0.7
    l = int(fs * dur)

### B ####
    sig, tt = chirp(f0, u, fs, dur)
    fig, axs = plt.subplots(2)
    axs[1].plot(tt[-200:], sig[-200:])
    axs[0].plot(tt[:200], sig[:200])
    fig.show()
    sd.play(sig, fs)

#### C ####

    xnoise = np.random.randn(l)
    tstart = 9
    nstart = int(tstart * fs)
    nsig = int(fs * tsig)
    xnoise[nstart: nstart + nsig] += sig
