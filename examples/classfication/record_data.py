import pickle
from os import path
import argparse
import time

from wirehead.connectors import EEGClickConnector

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--t")
    args = parser.parse_args()

    if args.t in ["alert", "notalert"]:
        PATH = path.join("data", args.t)
        N = 245 * 20 # how many samples per file
        BAUDRATE = 19200 # how many bits are being transferred per sec
        connection = EEGClickConnector(BAUDRATE, 1, None)

        print(f"Starting in 2 seconds, approximated time: {N/245:.2f} seconds")
        samples = []
        time.sleep(2)
        while len(samples) < N:
            samples.append(connection.read())

        connection.disconnect()
        print("Ready")

        i = 0
        while path.exists(path.join(PATH, f"sample_{i}.pickle")): i+=1
        with open(path.join(PATH, f"sample_{i}.pickle"), 'wb') as f:
            pickle.dump(samples, f)
    else:
        print("Please give correct state with verbose --t")
