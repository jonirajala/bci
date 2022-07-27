from statistics import mean
import matplotlib.pyplot as plt

from transform_data import load_and_transform_data
#ret = {"delta" : [], "theta lower" : [], "theta upper" : [],  "alpha lower" : [], "alpha upper" : [],"beta lower" : [], "beta upper" : [], "gamma" : [], "gamma upper": []}

if __name__ == "__main__":
    data = load_and_transform_data(transform="continious")
    averages = {"alert" : [], "notalert": []}
    for state in data.keys():
        for freq_index in range(len(data[state][0])):
            averages[state].append(mean([sample[freq_index] for sample in data[state]]))
        #ret = {"delta" : [], "theta lower" : [], "theta upper" : [],  "alpha lower" : [], "alpha upper" : [],"beta lower" : [], "beta upper" : [], "gamma" : [], "gamma upper": []}
    print("delta, theta lower, theta upper, alpha lower, alpha upper, beta lower, beta upper. gamma, gamma upper")
    print(averages['alert'])
    print(averages["notalert"])

    fig, ax = plt.subplots(2)
    x = [i for i in range(1,10)]

    ax[0].bar(x, averages["alert"])
    ax[1].bar(x, averages["notalert"])
    plt.show()