# import re
# import nltk
# import numpy as np
# from nltk.tokenize import RegexpTokenizer
# from nltk.tokenize import word_tokenize
# from nltk.corpus import sentiwordnet as swn
# from nltk.corpus import stopwords
# from nltk.stem import WordNetLemmatizer

# import tweepy 5 =1
# import time

# ckey = "---- Enter your own key -----"
# csecret = "---- Enter your own key -----"
# atoken = "---- Enter your own key -----"
# asecret = "---- Enter your own key -----"

# auth = tweepy.OAuthHandler(ckey,csecret)
# time.sleep(1)
# auth.set_access_token(atoken,asecret)
# time.sleep(1)
# api = tweepy.API(auth)
# time.sleep(1)

# s_query = 'iphone'+'-filter:retweets'
# tweets = tweepy.Cursor(api.search,	q=s_query,	lang='en').items(10)


# s_list = set(stopwords.words('english'))
# neg_words = np.array(['no' , 'not' , 'nor' , 'neither' , 'never' , 't' , 'nt' ,'aint'])

# for l1 in posComment:
# 	# === 1- removing numbers
# 	num_free = re.sub(r'\d+' , '' , l1)
# 	# print(num_free)

# 	# === 2- lower case
# 	lower_case = num_free.lower()
# 	# print(lower_case)

# 	# === 3- removing links
# 	pattern = re.compile('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
# 	link_free = pattern.sub('' , lower_case)
# 	# print(link_free)

# 	# === 4- removing names containing @
# 	pattern = re.compile('@(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
# 	user_free = pattern.sub('' , link_free)
# 	print('\n',user_free)

# 	# === 5- removing punctuations and tokenizing
# 	tokenizer = RegexpTokenizer(r'\w+')
# 	tokenized = tokenizer.tokenize(user_free)
# 	# print(tokenized)

# 	checkarr = np.array([])
# 	for l2,l3 in enumerate(tokenized):
# 		if l3 in neg_words:
# 			try:
# 				checkarr = np.append(checkarr,tokenized[l2+1])
# 			except:
# 				pass

# 	# === 6- POS tagging
# 	pos_tagged = nltk.pos_tag(tokenized)
# 	# print(pos_tagged)

# 	# === 8- Lemmatizer	
# 	lemmatizer = WordNetLemmatizer()
# 	lemmatized = np.array([])
# 	for l2 in pos_tagged:
# 		lemmatized = np.append(lemmatized,lemmatizer.lemmatize(l2[0]))
# 	# print(lemmatized)

# 	for l2,l3 in enumerate(checkarr):
# 		checkarr[l2] = lemmatizer.lemmatize(l3)

# 	# === 7- removing stopwords
# 	filtered = np.array([])
# 	for l2 in lemmatized:
# 		if l2 not in s_list:
# 			filtered = np.append(filtered,l2)

# 	# === 9- Polarity
# 	p_score = 0
# 	n_score = 0
# 	total_score = 0

# 	for l2 in filtered:
# 		try:
# 			senti = swn.senti_synsets(l2)
# 			polarity = list(senti)[0]
# 			if l2 not in checkarr:
# 				if polarity.pos_score() > polarity.neg_score():
# 					p_score += polarity.pos_score()

# 				if polarity.pos_score() < polarity.neg_score():
# 					n_score += polarity.neg_score()
# 			else:
# 				if polarity.pos_score() > polarity.neg_score():
# 					n_score += polarity.pos_score()

# 				if polarity.pos_score() < polarity.neg_score():
# 					p_score += polarity.neg_score()
# 		except:
# 			pass

# 	total_score = p_score - n_score

# 	# scoring scheme negative  > -0.125 neutral 0.125 < positive
# 	print('++++++ : ',total_score)

# 	if total_score < -0.125:
# 		print('negative')
# 	elif total_score > 0.125:
# 		print('positive')
# 	else:
# 		print('neutral')
# 	print('----------------------------------------------')


