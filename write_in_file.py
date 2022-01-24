
from sklearn.datasets import fetch_20newsgroups

#Definition du dictionnaire des categories

training_data = fetch_20newsgroups(subset='train', categories=['sci.med'], shuffle=True, random_state=5)
print(training_data.data[0])
file = "sci_med.txt"
f = open(file, 'w')
f.write(training_data.data[0])

