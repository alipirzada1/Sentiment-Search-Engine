import random
import re
import pickle
import collections

from sklearn import svm
from sklearn.metrics import accuracy_score

document = []
features = []
feature_set = []
n_matrix = []
labels = []
training_set = []
training_labels = []
testing_set = []
testing_labels = []

p_shifters = ['no' , 'not' , 'nor' , 'neither' , 'never' , 't' , 'nt' ,'aint' , 'but' , 'only', 'onli' , 'and' , 'for' , 'or' , 'yet' , 'so']

with open('pickleStopwords.txt', 'rb') as fl:
	s_list = pickle.load(fl)

with open('pickleTokenizer.txt' , 'rb') as fl:
	tokenizer = pickle.load(fl)

with open('pickleLemmatizer.txt' , 'rb') as fl:
	lemmatizer = pickle.load(fl)

with open('pickleStemmer.txt' , 'rb') as fl:
	stemmer = pickle.load(fl)



def DataRead(filename , label):

	fl = open(filename , "r").read()
	for l in fl.split("\n"):

		txt = re.sub(r'\d+' , '' , l)
		txt = txt.lower()
		txt = tokenizer.tokenize(txt)
		filtered = []

		for m in txt:
			if m in p_shifters:
				filtered.append(lemmatizer.lemmatize(stemmer.stem(m)))
				features.append(lemmatizer.lemmatize(stemmer.stem(m)))

			elif m not in s_list:
				filtered.append(lemmatizer.lemmatize(stemmer.stem(m)))
				features.append(lemmatizer.lemmatize(stemmer.stem(m)))
			else:
				pass

		document.append([filtered , label])


print("Reading Data =========================")
DataRead('positive.txt' , 'pos')
DataRead('neutral.txt' , 'neu')
DataRead('negative.txt' , 'neg')

print("Feature Set Creation =========================")
features = list(collections.Counter(features).most_common(1000))

for l in features:
	feature_set.append(l[0])

random.shuffle(document)
print("Total Instances ", len(document) ," =========================")

with open('pickleFeatures.txt' , 'wb') as fl:
	pickle.dump(feature_set , fl)

print("N Matrix Creation =========================")
for l in document:
	count = collections.Counter(l[0])
	n_matrix.append([count[m] for m in feature_set])
	labels.append(l[1])

training_set = n_matrix[:40000]
training_labels = labels[:40000]

testing_set = n_matrix[40000:]
testing_labels = labels[40000:]

classifier = svm.SVC(kernel='linear', decision_function_shape='ovr')

print("Training SVM =========================")
classifier.fit(training_set , training_labels)

with open('pickleClassifier.txt' , 'wb') as fl:
	pickle.dump(classifier , fl)

print("Testing SVM =========================")
predicted = classifier.predict(testing_set)


print("SVM Accuracy is : " , accuracy_score(testing_labels , predicted) * 100 , '\n\n')
print("Done =========================")