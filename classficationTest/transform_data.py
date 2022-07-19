import os
import pickle

from wirehead.transforms import wavelet_transform, fft

def load_raw_data():
    ret = {"alert":[], "notalert":[]} # dict which contains 2 lists, one for alert samples and one for not alert samples
    for state in ["alert", "notalert"]:
        for filename in os.listdir(os.path.join("data", state)):
            print(os.path.join("data", state))
            with open(os.path.join("data", state,filename), 'rb') as f:
                sample = pickle.load(f)
            ret[state] += sample
    return ret


def load_and_transform_data():
    sampling_window = 245
    sampling_freq = 245
    data = load_raw_data()
    for state, samples in data.items():
        transformed_data = []
        for i in range(len(samples)//sampling_window):
            transformed_data += [wavelet_transform(samples[i*sampling_window:(i+1)*sampling_window])]
        data[state] = transformed_data
    return data