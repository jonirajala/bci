import warnings
import numpy as np
import matplotlib.pyplot as plt
import pywt
from scipy.stats.mstats import gmean
from statistics import mean
import time

try:
    from .utils import random_signal
except:
    from utils import random_signal

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

def continuous_wavelet_transform(signal, sampling_freq):
    bin_ranges = [1, 4, 6, 8, 10, 13, 20, 30, 60, 200]
    n_scales = 786 // 4
    scales = np.linspace(1.5, 80, n_scales)
    ret = [[],[],[],[],[],[],[],[],[]]
    cA, cD = pywt.cwt(signal, scales, 'morl', 1 / sampling_freq)
    powers = np.mean((abs(cA) ** 2), 1)
    bin_indices = np.digitize(cD, bin_ranges)
    for bin_index, power_spectrum in zip(bin_indices, powers):
        ret[bin_index-1].append(power_spectrum)
    ret = [np.log2(float(mean(i))) for i in ret]
    
    return ret 

def discrete_wavelet_transform(signal):
    coeffs = pywt.wavedec(signal, 'db3', level=3)
    cA3, cD3, cD2, cD1 = coeffs
    return cA3

if __name__ == "__main__":
    signal = random_signal()
    #signal = np.array((1,2,3,4))
    # dt = 1/128
    # ffts, freqs = fft(signal, dt)
    # print(ffts)
    # figure, axis = plt.subplots(2, 1)

    # axis[0].plot(freqs, ffts)
    # axis[1].plot(signal)
    # plt.show()

    freq = 240
    f = continuous_wavelet_transform(signal, freq)
    print(f)