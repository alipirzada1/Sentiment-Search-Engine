
# import nltk
# import random
# import numpy as np

# from nltk.corpus import movie_reviews
# from nltk.classify.scikitlearn import SklearnClassifier
# from sklearn.svm import SVC, LinearSVC 	, NuSVC

# documents = [(list(movie_reviews.words(fileid)),category)
# 			for category in movie_reviews.categories()
# 			for fileid in movie_reviews.fileids(category)]


# random.shuffle(documents)

# print(documents[1])

# all_words = []

# for w in movie_reviews.words():
# 	all_words.append(w.lower())

# all_words = nltk.FreqDist(all_words)

# word_features = list(all_words.keys())[:3000]

# def find_features(document):
# 	word = set(document)
# 	features = {}
# 	for w in word_features:
# 		features[w] = (w in word)

# 	return features

# print((find_features(movie_reviews.words('neg/cv000_29416.txt'))))

# featuresets = [(find_features(rev), category) for (rev , category) in documents]

# training_set = featuresets[:1900]
# testing_set = featuresets[1900:]

# NBclassifier = nltk.NaiveBayesClassifier.train(training_set)
# NBclassifier.show_most_informative_features(15)
# print("\n\nNaive Bayes Classifier Accuracy Percentage : " , (nltk.classify.accuracy(NBclassifier, testing_set))*100)

# SVCclassifier = SklearnClassifier(SVC())
# SVCclassifier.train(training_set)
# print("\n\nSVC Classifier Accuracy Percentage : " , (nltk.classify.accuracy(SVCclassifier, testing_set))*100)

# LinearSVCclassifier = SklearnClassifier(SVC())
# LinearSVCclassifier.train(training_set)
# print("\n\nLinearSVM classifier Accuracy Percentage : " , (nltk.classify.accuracy(LinearSVCclassifier, testing_set))*100)

# NuSVCclassifier = SklearnClassifier(SVC())
# NuSVCclassifier.train(training_set)
# print("\n\nNuSVC Classifier Accuracy Percentage : " , (nltk.classify.accuracy(NuSVCclassifier, testing_set))*100)

# ================================================

# ================================================


# from nltk import *
# arr = ['work','work','work','work','test','test','test','test','test','success']
# print(arr)
# arr = FreqDist(arr)
# print(arr)
# print(arr.most_common(2))
# print(list(arr.keys()))

# ================================================

# ================================================

# matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# matrix2 = ['three','five','eleven']

# train_set = matrix[:2]
# train_label = matrix2[:2]

# test_set = matrix[2:]
# test_label = matrix2[2:]

# print(train_set)
# print(train_label)
# print(test_set)
# print(test_label)


# b_matrix = []
# for i in matrix:
# 	check_arr = []
# 	for j in matrix2:
# 		if j in i:
# 			check_arr.append(1)
# 		else:
# 			check_arr.append(0)
# 	b_matrix.append(list(check_arr))

# print(b_matrix)

# ======================================================

# ======================================================

# import pickle

# filehandle = open('dummmyFile.txt','wb')
# var = [1,2,3,4,5]
# pickle.dump(var, filehandle)
# filehandle.close()
# filehandle = open('dummmyFile' , 'rb')
# var = pickle.load(filehandle)
# print(var)

# ==========================================================

# ==========================================================

# import timeit
# import time

# start = timeit.default_timer()
# time.sleep(5)
# end = timeit.default_timer()
# print(end - start)

# ==========================================================

# ==========================================================

# import time
# import threading

# class myThread (threading.Thread):
# 	def __init__(self, threadId, name, counter):
# 		threading.Thread.__init__(self)
# 		self.threadID = threadID
# 		self.name = name
# 		self.counter = counter

# 	def run(self):
# 		print "Starting " + self.name
# 		print_time(self.name, 5, self.counter)
# 		print "Exiting " + self.name


# ==================================================

# ==================================================

# import nltk
# import pickle

# from nltk.tokenize import RegexpTokenizer
# from nltk.tokenize import word_tokenize
# from nltk.corpus import stopwords
# from nltk.stem import WordNetLemmatizer

# print(list(stopwords.words('english')))

# filehandle = open('tokenizer.txt' , 'wb')
# tokenizer = RegexpTokenizer(r'\w+')
# pickle.dump(tokenizer , filehandle)
# filehandle.close()

# filehandle = open('lemmatizer.txt' , 'wb')
# lemmatizer = WordNetLemmatizer()
# pickle.dump(lemmatizer , filehandle)
# filehandle.close()

# filehandle = open('stopwords.txt' , 'wb')
# slist = list(stopwords.words('english'))
# pickle.dump(slist , filehandle)
# filehandle.close()

# ========================================

# ========================================

# filehandle = open('tokenizer.txt' , 'rb')
# tokenizer = pickle.load(filehandle)
# filehandle.close()

# filehandle = open('lemmatizer.txt' , 'rb')
# lemmatizer = pickle.load(filehandle)
# filehandle.close()

# filehandle = open('stopwords.txt' , 'rb')
# slist = pickle.load(filehandle)
# filehandle.close()

# sentence = "A? quick! brown@ fox# jumps' over& the lazy dog"
# sentence = tokenizer.tokenize(sentence)
# print(sentence)


# ========================================

# ========================================

# word = ["looking"]

# arr = [['looking', 5] , ['doomed' , 2]]
# for i in word:
# 	for j in arr:
# 		if j[0] in i:
# 			print(j[1])


# ========================================

# ========================================

# import pandas as pd 
# import random
# from sklearn.utils import shuffle

# df = pd.read_csv('training.csv')
# print(df)

# ========================================

# ========================================

# import collections

# arr = ['apple','apple','apple','orange','orange','bananas']
# arr2 = []

# counter = collections.Counter(arr)
# print(counter)
# print(counter.values())
# print(list(counter.most_common(2)))
# print(counter['apple'])

# ========================================

# ========================================

# import pickle
# data = []
# with open('featureCount.txt' , 'rb') as fl:
# 	data = pickle.load(fl)
# for l in data:
# 	print(l)

# ========================================

# ========================================