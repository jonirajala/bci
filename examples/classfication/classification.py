from sklearn import svm
import random

from transform_data import load_and_transform_data

data = load_and_transform_data()

random.shuffle(data['alert'])
random.shuffle(data['notalert'])


# 0 alert, 1 notalert
test_size = 0.2

train_alert_x = data['alert'][:int(len(data['alert'])*(1-test_size))]
test_alert_x = data['alert'][int(len(data['alert'])*(test_size)):]

train_notalert_x = data['notalert'][:int(len(data['notalert'])*(1-test_size))]
test_notalert_x = data['notalert'][int(len(data['notalert'])*(test_size)):]

train_alert_y = [0] * len(train_alert_x)
test_alert_y = [0] * len(test_alert_x)

train_notalert_y = [1] * len(train_notalert_x)
test_notalert_y = [1] * len(test_notalert_x)

train_x = train_alert_x + train_notalert_x
train_y = train_alert_y + train_notalert_y

test_x = test_alert_x + test_notalert_x
test_y = test_alert_y + test_notalert_y


clf = svm.SVC()
clf.fit(train_x, train_y)

print(clf.score(test_x, test_y))
# Accuracy around 60-70%