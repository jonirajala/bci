from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
import random

from transform_data import load_and_transform_data

data = load_and_transform_data("continuous")


random.shuffle(data['alert'])
random.shuffle(data['notalert'])

# 0 alert, 1 notalert
test_size = 0.2

train_alert_x = data['alert'][:int(len(data['alert']) * (1-test_size))]
test_alert_x = data['alert'][int(len(data['alert']) * (1-test_size)):]

train_notalert_x = data['notalert'][:int(len(data['notalert'])*(1-test_size))]
test_notalert_x = data['notalert'][int(len(data['notalert'])*(1-test_size)):]

train_alert_y = [0] * len(train_alert_x)
test_alert_y = [0] * len(test_alert_x)

train_notalert_y = [1] * len(train_notalert_x)
test_notalert_y = [1] * len(test_notalert_x)

train_x = train_alert_x + train_notalert_x
train_y = train_alert_y + train_notalert_y

test_x = test_alert_x + test_notalert_x
test_y = test_alert_y + test_notalert_y


assert not any(i in test_x for i in train_x)

print(f"Test size {len(test_x)}, train size {len(train_x)}")

clf = svm.SVC()
clf.fit(train_x, train_y)
print(f"Accuracy with Support vector machine classifier: {clf.score(test_x, test_y):.2f} %")

RF = RandomForestClassifier(n_estimators=200, max_depth=None)
RF.fit(train_x, train_y)
print(f"Accuracy with Random forest classifier: {RF.score(test_x, test_y):.2f} %")
