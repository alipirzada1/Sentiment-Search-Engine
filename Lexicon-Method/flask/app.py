from flask import Flask, request, render_template

import re
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import word_tokenize
from nltk.corpus import sentiwordnet as swn
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import *
import tweepy
import time


# PREP CODE =========================

 # ================= TWEEPY

ckey = "---- Enter your own key -----"
csecret = "---- Enter your own key -----"
atoken = "---- Enter your own key -----"
asecret = "---- Enter your own key -----"





auth = tweepy.OAuthHandler(ckey,csecret)
time.sleep(1)
auth.set_access_token(atoken,asecret)
time.sleep(1)
api = tweepy.API(auth)

# ==================== NLTK

s_list = set(stopwords.words('english'))
neg_words = ['no' , 'not' , 'nor' , 'neither' , 'never' , 't' , 'nt' ,'aint']
tokenizer = RegexpTokenizer(r'\w+')
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()
pattern_link = re.compile('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
pattern_name = re.compile('@(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')




# FLASK CODE ===========================

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

		# === 1- removing numbers
		num_free = re.sub(r'\d+' , '' , l.full_text)

		# === 2- lower case
		lower_case = num_free.lower()

		# === 3- removing links
		link_free = pattern_link.sub('' , lower_case)

		# === 4- removing names containing @
		user_free = pattern_name.sub('' , link_free)

		# === 5- removing punctuations and tokenizing
		tokenized = tokenizer.tokenize(user_free)

		# === 6- POS tagging
		# pos_tagged = nltk.pos_tag(tokenized)

		# === 7- Stemmer
		stemmed = []
		for m in tokenized:
			# stemmed.append(stemmer.stem(m[0]))
			stemmed.append(stemmer.stem(m))

		# === 8- Lemmatizer	
		lemmatized = []
		for m in stemmed:
			# lemmatized.append(lemmatizer.lemmatize(m[0]))
			lemmatized.append(lemmatizer.lemmatize(m))

		# === 7- removing stopwords
		filtered = []
		for m in lemmatized:
			if m in neg_words:
				filtered.append(m)
			elif m not in s_list:
				filtered.append(m)
			else:
				pass


		# === 10- Polarity
		total_score = 0
		flag = 1
		for m in filtered:
			if m in neg_words:
				flag = flag * (-1)
			else:
				try:
					senti = swn.senti_synsets(m)
					polarity = list(senti)[0]

					if polarity.pos_score() > polarity.neg_score():
						total_score += ((polarity.pos_score())*flag)

					if polarity.pos_score() < polarity.neg_score():
						total_score -= ((polarity.neg_score())*flag)
				except:
					pass
					
				flag = 1

		# scoring scheme negative  > -0.125 neutral 0.125 < positive
		if  total_score > 0.125:
			posComment.append(user_free)
			posCount += 1

		elif total_score < -0.125:
			negComment.append(user_free)
			negCount += 1

		else:
			neuComment.append(user_free)
			neuCount += 1
		
	return render_template('results.html' , returned={'posComment':posComment , 'neuComment':neuComment , 'negComment':negComment , 'posCount':posCount , 'neuCount':neuCount , 'negCount':negCount })


if __name__ == '__main__':
    app.run(debug=True)





