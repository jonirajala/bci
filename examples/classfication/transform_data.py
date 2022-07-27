import os
import pickle

from tools.transforms import continuous_wavelet_transform, discrete_wavelet_transform, fft

def load_raw_data():
    print("Loading data...")
    ret = {"alert":[], "notalert":[]} # dict which contains 2 lists, one for alert samples and one for not alert samples
    for state in ["alert", "notalert"]:
        for filename in os.listdir(os.path.join("data", state)):
            if filename.endswith(".pickle"):
                try:
                    with open(os.path.join("data", state, filename), 'rb') as f:
                        sample = pickle.load(f)
                    sample = [float(x) for x in sample]
                    #print(f"Number of zeros: {sample.count(0.00)} out of {len(sample)}")
                    #print(f"Number of 1023: {sample.count(1023.00)} out of {len(sample)}")
                    sample = list(filter(lambda x: x != 0.00 and x != 1023.0, sample))
                    ret[state] += sample
                except Exception as e:
                    print(e)
                    print(f"File: {filename}")
    print("Data loading ready!")
    return ret

def load_and_transform_data(transform="discrete"):
    sampling_window = 480
    sampling_freq = 240
    data = load_raw_data()
    print("Transforming data")
    for state, samples in data.items():
        transformed_data = []
        for i in range(len(samples)//sampling_window):
            if len(samples[i*sampling_window:(i+1)*sampling_window]) == sampling_window:
                if transform == "discrete":
                    transformed_data += [discrete_wavelet_transform(samples[i*sampling_window:(i+1)*sampling_window])]
                else:
                    transformed_data += [continuous_wavelet_transform(samples[i*sampling_window:(i+1)*sampling_window], sampling_freq)]
            else:
                print("Missing data")
        data[state] = transformed_data
    print("Data transformed")

    return data

if __name__ == "__main__":
    data = load_and_transform_data("continuous")
    print(data)