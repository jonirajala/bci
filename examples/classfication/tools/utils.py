from tkinter import Menu
import numpy as np
import time
from collections import deque
import serial
from statistics import mean, variance

try:
    from .connectors import EEGClickConnector
except ImportError:
    from connectors import EEGClickConnector

def random_signal():
    x = np.linspace(0, 1000, 300)
    y = 0
    result = []
    for _ in x:
        result.append(y)
        y += np.random.normal(scale=1)
    return np.array(result)

def calculate_sampling_freq():
    BAUDRATE = 19200
    connection = EEGClickConnector(BAUDRATE, 1, None)
    samples = []
    times = []
    time.sleep(5)
    s = time.time()
    for i in range(1000):
        #s = time.time()
        #print("len of buffer: ", connection.connection.inWaiting())
        samples.append(connection.read())
        #signal = connection.read()
        #print("len of read: ", len(signal.encode("utf-8")), "signal: ", signal)
        #e = time.time()
        #times.append(e-s)
    e = time.time()
    #print(mean(times))
    #print(variance(times))
    print(f'FPS: {len(samples) / ( e - s ):.2f}')

if __name__ == "__main__":
    calculate_sampling_freq()