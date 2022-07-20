from statistics import mean

from transform_data import load_and_transform_data
#ret = {"delta" : [], "theta lower" : [], "theta upper" : [],  "alpha lower" : [], "alpha upper" : [],"beta lower" : [], "beta upper" : [], "gamma" : [], "gamma upper": []}

if __name__ == "__main__":
    print("Loading data...")
    data = load_and_transform_data(transform="continious")
    print("Data loading ready!")
    print(data['alert'])
    averages = {"alert" : [], "notalert": []}
    for state in data.keys():
        for freq_index in range(len(data[state][0])):
            print(data[state][0][freq_index])
            averages[state].append(mean( [sample[freq_index] for sample in data[state]] ))
        # print(data[state])
        # for freq in data[state].keys():
        #     averages[state].append(mean(sample[freq] for sample in data[state]))

    print(averages)



    
