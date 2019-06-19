from flask import Flask , render_template , request

import re
import tweepy
import pickle
import os
import time
import collections



# Prep Code ============================
my_dir = os.path.dirname(__file__)

# file_path = os.path.join(my_dir, 'pickle/pickleClassifier45k.txt')
with open('pickle/pickleClassifier45k.txt','rb') as fl:
# with open(file_path,'rb') as fl:
	classifier = pickle.load(fl)

# file_path = os.path.join(my_dir, 'pickle/pickleFeatures45k.txt')
with open('pickle/pickleFeatures45k.txt', 'rb') as fl:
# with open(file_path, 'rb') as fl:
	feature_set = pickle.load(fl)

# file_path = os.path.join(my_dir, 'pickle/Lemmatizer.txt')
with open('pickle/Lemmatizer.txt', 'rb') as fl:
# with open(file_path, 'rb') as fl:
	lemmatizer = pickle.load(fl)

# file_path = os.path.join(my_dir, 'pickle/Stemmer.txt')
with open('pickle/Stemmer.txt', 'rb') as fl:
# with open(file_path, 'rb') as fl:
	stemmer = pickle.load(fl)

# file_path = os.path.join(my_dir, 'pickle/Stopwords.txt')
with open('pickle/Stopwords.txt', 'rb') as fl:
# with open(file_path, 'rb') as fl:
	stopwords = pickle.load(fl)

# file_path = os.path.join(my_dir, 'pickle/Tokenizer.txt')
with open('pickle/Tokenizer.txt', 'rb') as fl:
# with open(file_path, 'rb') as fl:
	tokenizer = pickle.load(fl)

neg_words = ['no' , 'not' , 'nor' , 'neither' , 'never' , 't' , 'nt' ,'aint']

ckey = "---- Enter your own key -----"
csecret = "---- Enter your own key -----"
atoken = "---- Enter your own key -----"
asecret = "---- Enter your own key -----"




# time.sleep(2)
auth = tweepy.OAuthHandler(ckey,csecret)
# time.sleep(1)
auth.set_access_token(atoken,asecret)
# time.sleep(1)
api = tweepy.API(auth)


# Flask Codes ============================

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')
	
@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/results' , methods=['POST'])
def results():

	if request.form['searchBtn'] == 'searchQuery':
		key = request.form['searchQuery']

	if request.form['searchBtn'] == 'searchSelect':
		key = request.form['searchSelect']

	try:
		query = str(key)+'-filter:retweets'
		tweets = tweepy.Cursor(api.search, q=query, lang='en', tweet_mode='extended').items(150)
	except:
		posComment = "You are seeing this beacuse the application is on free server and the CPU limit is over try again after 15 hrs"
		neuComment = "You are seeing this beacuse the application is on free server and the CPU limit is over try again after 15 hrs"
		negComment = "You are seeing this beacuse the application is on free server and the CPU limit is over try again after 15 hrs"

	posComment = []
	neuComment = []
	negComment = []

	posCount = 0
	neuCount = 0
	negCount = 0

	for l in tweets:

		data = l.full_text

		# === 1- lower case
		data = data.lower()

		# === 2- removing numbers
		data = re.sub(r'\d+' , '' , data)

		# === 3- removing links
		pattern = re.compile('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
		data = pattern.sub('' , data)

		# === 4- removing names containing @
		pattern = re.compile('@(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
		data = pattern.sub('' , data)
		
		readable = data

		filtered = []
		data = tokenizer.tokenize(data)

		for w in data:
			if w in neg_words:
				filtered.append(lemmatizer.lemmatize(stemmer.stem(w)))
			elif w not in stopwords:
				filtered.append(lemmatizer.lemmatize(stemmer.stem(w)))
			else:
				pass

		n_matrix = []

		count = collections.Counter(filtered)

		for w in feature_set:
			n_matrix.append(count[w])

		prediction = classifier.predict([n_matrix])

		if prediction == 'pos':
			posComment.append(readable)
			posCount+=1
		elif prediction == 'neg':
			negComment.append(readable)
			negCount+=1
		else:
			neuComment.append(readable)
			neuCount+=1

	return render_template('results.html' , returned={'posComment':posComment , 'neuComment':neuComment , 'negComment':negComment , 'posCount':posCount , 'neuCount':neuCount , 'negCount':negCount })


if __name__ == '__main__':
    app.run()
