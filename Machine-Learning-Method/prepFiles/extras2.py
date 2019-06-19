# import json
# import nltk
# import random
# import re
# import collections
# import timeit
# import pickle

# from sklearn import svm
# from sklearn.metrics import accuracy_score

# p_shifters = ['no' , 'not' , 'nor' , 'neither' , 'never' , 't' , 'nt' ,'aint' , 'but' , 'only', 'onli']

# with open('pickleStopwords.txt' , 'rb') as fl:
# 	s_list = pickle.load(fl)

# with open('pickleStemmer.txt' , 'rb') as fl:
# 	stemmer = pickle.load(fl)

# with open('pickleLemmatizer.txt' , 'rb') as fl:
# 	lemmatizer = pickle.load(fl)

# with open('pickleTokenizer.txt' , 'rb') as fl:
# 	tokenizer = pickle.load(fl)

# document = []
# features = []
# feature_set = []
# n_matrix = []
# labels = []
# training_set = []
# training_labels = []
# testing_set = []
# testing_labels = []

# # print("Reading Data (This will take time) - - -  ")
# file = open('dummyJson20.json','r')

# startT = timeit.default_timer()
# for l in file.readlines():
# 	filtered = []
# 	raw = json.loads(l)
# 	txt = raw['reviewText']
# 	txt = re.sub(r'\d+' , '' , txt)
# 	txt = txt.lower()
# 	txt = tokenizer.tokenize(txt)

# 	for w in txt:
# 		if w in p_shifters:
# 			filtered.append(lemmatizer.lemmatize(stemmer.stem(w)))
# 			features.append(lemmatizer.lemmatize(stemmer.stem(w)))
# 		elif w not in s_list:
# 			filtered.append(lemmatizer.lemmatize(stemmer.stem(w)))
# 			features.append(lemmatizer.lemmatize(stemmer.stem(w)))
# 		else:
# 			pass
# 	if raw['overall'] > 3:
# 		document.append([filtered , 'pos'])
# 	elif raw['overall'] < 3:
# 		document.append([filtered , 'neg'])
# 	else:
# 		document.append([filtered , 'neu'])

# endT = timeit.default_timer()

# # with open('details.txt','a') as fl:
# # 	details = "Data Read Time is : " + str((endT - startT)/60) + '\n'
# # 	fl.write(details)


# random.shuffle(document)

# features = collections.Counter(features)
# for l in list(features.most_common(10)):
# 	feature_set.append(l[0])

# print(feature_set)
# exit()
# # with open('pickleFeatures.txt' , 'wb') as fl:
# # 	pickle.dump(feature_set , fl)

# # print("Making Numeric Matrix (This will take time) - - -  ")

# startT = timeit.default_timer()
# for l in document:
# 	count = collections.Counter(l[0])
# 	data = []
# 	for w in feature_set:
# 		data.append(count[w])
	
# 	n_matrix.append(data)
# 	labels.append(l[1])

# endT = timeit.default_timer()

# # with open('details.txt','a') as fl:
# # 	details = "Making Numeric Matrix Time : " + str((endT - startT)/60) + '\n'
# # 	fl.write(details)

# training_set = n_matrix[:45000]
# training_labels = labels[:45000]

# testing_set = n_matrix[45000:]
# testing_labels = labels[45000:]

# classifier = svm.SVC(kernel='linear', decision_function_shape='ovr')

# # with open('pickleClassifier.txt' , 'rb') as fl:
# # 	classifier = pickle.load(fl)

# print('Training SVM (This will take time) - - -')
# startT = timeit.default_timer()
# classifier.fit(training_set , training_labels)
# endT = timeit.default_timer()
# # with open('details.txt','a') as fl:
# # 	details = "Training at 1000 features and 45k instances Time is : " + str((endT - startT)/60) + '\n'
# # 	fl.write(details)

# # with open('pickleClassifier.txt', 'wb') as fl:
# # 	pickle.dump(classifier , fl)

# print('Testing SVM - - -')
# startT = timeit.default_timer()
# predicted = classifier.predict(testing_set)
# endT = timeit.default_timer()

# # with open('details.txt','a') as fl:
# # 	details = "Testing at 5k samples Time is : " + str((endT - startT)/60) + '\n'
# # 	fl.write(details)

# print("SVM Accuracy is : " , accuracy_score(testing_labels , predicted) * 100 , '\n\n')

# # with open('details.txt','a') as fl:
# # 	details = "SVM Accuracy is : " + str(accuracy_score(testing_labels , predicted) * 100) + '\n'
# # 	fl.write(details)
# # 	fl.write('=================================================\n')
