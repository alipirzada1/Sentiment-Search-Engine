# import nltk
# import re
# import random
# import pickle
# import collections
# import timeit

# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize
# from nltk.tokenize import RegexpTokenizer
# from nltk.stem import WordNetLemmatizer
# from sklearn import svm
# from sklearn.metrics import accuracy_score

# pos_file = open('positive.txt', 'r').read()
# neg_file = open('negative.txt', 'r').read()

# document = []
# features = []
# feature_set = []
# n_matrix = []
# labels = []
# training_set = []
# training_labels = []
# testing_set = []
# testing_labels = []

# s_list = set(stopwords.words('english'))
# neg_words = ['no' , 'not' , 'nor' , 'neither' , 'never' , 't' , 'nt' ,'aint' , 'but']

# startT = timeit.default_timer()

# for r in pos_file.split('\n'):

# 	filtered = []

# 	txt = re.sub(r'\d+' , '' , r)
# 	txt = txt.lower()
# 	tokenizer = RegexpTokenizer(r'\w+')
# 	txt = tokenizer.tokenize(txt)
# 	lemmatizer = WordNetLemmatizer()

# 	for w in txt:
# 		if w in neg_words:
# 			filtered.append(lemmatizer.lemmatize(w))
# 		elif w not in s_list:
# 			filtered.append(lemmatizer.lemmatize(w))
# 			# filtered.append(w)
# 		else:
# 			pass


# 	document.append([filtered, 'pos'])


# for r in neg_file.split('\n'):

# 	filtered = []
	
# 	txt = re.sub(r'\d+' , '' , r)
# 	txt = txt.lower()
# 	tokenizer = RegexpTokenizer(r'\w+')
# 	txt = tokenizer.tokenize(txt)

# 	for w in txt:
# 		if w in neg_words:
# 			filtered.append(lemmatizer.lemmatize(w))
# 			features.append(lemmatizer.lemmatize(w))
# 		elif w not in s_list:
# 			filtered.append(lemmatizer.lemmatize(w))
# 			features.append(lemmatizer.lemmatize(w))
# 		else:
# 			pass

# 	document.append([filtered , 'neg'])

# endT = timeit.default_timer()
# with open('details.txt' , 'a') as fl:
# 	line = "Data Read Time is : " + str(endT - startT) + '\n'
# 	fl.write(line)
# with open('details.txt' , 'a') as fl:
# 	fl.write("working")

# with open('details.txt' , 'a') as fl:
# 	fl.write("working")
# exit()
# random.shuffle(document)

# # features = collections.Counter(features)
# # # for l in list(features.most_common(2000)):
# # for l in list(features.most_common(1500)):
# # 	feature_set.append(l[0])

# with open('pickleFS' , 'rb') as fl:
# 	feature_set = pickle.load(fl)


# print("Making Numeric Matrix (This will take time) - - -  ")

# for l in document:
# 	count = collections.Counter(l[0])
# 	data = []
# 	for w in feature_set:
# 		data.append(count[w])
	
# 	n_matrix.append(data)
# 	labels.append(l[1])

# training_set = n_matrix[:7000]
# training_labels = labels[:7000]

# testing_set = n_matrix[7000:]
# testing_labels = labels[7000:]

# # classifier = svm.LinearSVC()
# # print('\nTraining SVM (This will take time) - - -\n')
# # classifier.fit(training_set , training_labels)

# with open('pickleCLS' , 'rb') as fl:
# 	classifier = pickle.load(fl)

# print('\nTesting SVM - - - \n')
# predicted = classifier.predict(testing_set)
# print("\nSVM Accuracy is : " , accuracy_score(testing_labels , predicted) * 100 , '\n\n')