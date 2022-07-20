import numpy as np
import time
from collections import deque
import serial

from .connectors import EEGClickConnector

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
    fps_counter = deque(maxlen=50)
    last_print = time.time()
    while True:
        connection.read()
        fps_counter.append(time.time() - last_print + 7.414817810058594e-05) # mocks the append to signals list, 
        #7.414817810058594e-05 is approximately the time to compute next two lines
        last_print = time.time() # excess computing
        #print(f'FPS: {len(fps_counter)/sum(fps_counter):.2f}') # excess computing
        print(f'FPS: {1/(sum(fps_counter)/len(fps_counter)):.2f}')
    

# last_print = time.time()
# fps_counter = deque(maxlen=50)
# sequence = np.zeros((100,1))
# counter = 0
# def calculate_sampling_freq():


#     def print_raw(sample):
#         global last_print
#         global sequence
#         global counter

#         sequence = np.roll(sequence, 1, 0)
#         sequence[0, ...] = sample

#         fps_counter.append(time.time() - last_print)
#         last_print = time.time()
#         print(f'FPS: {1/(sum(fps_counter)/len(fps_counter)):.2f}')

#     BAUDRATE = 14400
#     connection = EEGClickConnector(BAUDRATE, 1, None)

#     fps_counter = []
#     last_print = time.time()
#     while True:
#         samp = connection.read()
#         print_raw((samp))

if __name__ == "__main__":
    calculate_sampling_freq()