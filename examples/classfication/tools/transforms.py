import enum
import warnings
import numpy as np
import matplotlib.pyplot as plt
import pywt
from scipy.stats.mstats import gmean
from statistics import mean

from .utils import random_signal

def fft(sig, dt=None):
    # Here it's assumes analytic signal (real signal...) - so only half of the axis is required
    if dt is None:
        dt = 1
        t = np.arange(0, sig.shape[-1])
        xLabel = 'samples'
    else:
        t = np.arange(0, sig.shape[-1]) * dt
        xLabel = 'freq [Hz]'
    if sig.shape[0] % 2 != 0:
        warnings.warn("signal preferred to be even in size, autoFixing it...")
        t = t[0:-1]
        sig = sig[0:-1]
    sigFFT = np.fft.fft(sig) / t.shape[0]  # Divided by size t for coherent magnitude
    freq = np.fft.fftfreq(t.shape[0], d=dt)
    firstNegInd = np.argmax(freq < 0)
    freqAxisPos = freq[0:firstNegInd]
    sigFFTPos = np.abs(2 * sigFFT[0:firstNegInd])  # *2 because of magnitude of analytic signal
    return sigFFTPos, freqAxisPos

def continious_wavelet_transform(signal):
    # import time
    # s = time.time()
    # We calculated the coefﬁcients of CWT from Eq. (1) for thescale range of [1.5-80] with a scale-step of 0.1 for all subjects.
    # Next,we computed the geometric mean power spectrum of thewavelet coefﬁcients of each phase
    BIN_RANGES = [1, 4, 6, 8, 10, 13, 20, 30, 60, 200]
    SAMP_FREQ = 245
    TOTAL_NUM_OF_SCALES = 786
    SCALES = np.linspace(1.5, 80, TOTAL_NUM_OF_SCALES)
    #ret = {"delta" : [], "theta lower" : [], "theta upper" : [],  "alpha lower" : [], "alpha upper" : [],"beta lower" : [], "beta upper" : [], "gamma" : [], "gamma upper": []}
    ret = [[]] * 9
    cA, cD = pywt.cwt(signal, SCALES, 'morl', 1 / SAMP_FREQ)
    power_spectrums = []
    for coefs in cA:
        sums = 0
        for coef in coefs:
            sums += abs(coef)**2
        sums /= len(coefs)
        power_spectrums.append(sums)

    bin_indices = np.digitize(cD, BIN_RANGES)

    for bin_index, power_spectrum in zip(bin_indices, power_spectrums):
        #print(bin_index, power_spectrum)
        ret[bin_index-1].append(power_spectrum)

    assert ret[0] == ret[1] == ret[2]

    for i in range(len(ret)):
        ret[i] = int(mean(ret[i]))
    #e = time.time()
    #print(f"took: {e-s} seconds")

    return ret

def discrete_wavelet_transform(signal):
    coeffs = pywt.wavedec(signal, 'db3', level=3)
    cA3, cD3, cD2, cD1 = coeffs
    return cA3


if __name__ == "__main__":
    # #signal = random_signal()
    signal = np.array((1,2,3,4))
    # dt = 1/128
    # ffts, freqs = fft(signal, dt)
    # print(ffts)
    # figure, axis = plt.subplots(2, 1)

    # axis[0].plot(freqs, ffts)
    # axis[1].plot(signal)
    # plt.show()

    f = wavelet_transform(signal)
    print(f)