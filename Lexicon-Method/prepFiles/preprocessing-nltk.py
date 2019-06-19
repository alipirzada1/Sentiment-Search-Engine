# import re
# import numpy as np
# import nltk

# from nltk.tokenize import RegexpTokenizer
# from nltk.stem.snowball import *
# from nltk.stem.porter import *
# from nltk.tokenize import word_tokenize
# from nltk.corpus import stopwords
# from nltk.corpus import sentiwordnet as swn
# from nltk.stem import WordNetLemmatizer

# sentence = 'this phone is not good'


# # === 1- lower case
# txt = sentence.lower()

# # ===	 2- removing numbers
# txt = re.sub(r'\d+' , '' , txt)


# # === 3- removing links
# pattern = re.compile('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
# txt = pattern.sub('' , txt)


# # === 4- removing names containing @
# pattern = re.compile('@(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
# txt = pattern.sub('' , txt)
# print(txt)

 
# # # === 5- removing punctuations and tokenize
# tokenizer = RegexpTokenizer(r'\w+')
# txt = tokenizer.tokenize(sentence)
# txt = nltk.pos_tag(txt)



# neg_words = np.array(['no' , 'not' , 'nor' , 'neither' , 'never' , 't' , 'nt' ,'aint'])
# checkarr = np.array([])
# for l in neg_words:
# 	if l in txt:
# 		checkarr = np.checkarr(checkarr,l)


# # === 6- removing stopwords
# s_list = set(stopwords.words('english'))
# filtered = np.array([])
# for loop in txt:
# 	if loop not in s_list:
# 		filtered = np.append(filtered,loop)

# # # === 7- Stemming (SnowBall Algorithm)
# stemmer = SnowballStemmer("english")
# for loop in filtered:
# 	print(stemmer.stem(loop))

# # # === 7- Stemming (Porter Algorithm)
# stemmer = PorterStemmer()
# for loop in filtered:
# 	print(stemmer.stem(loop))

# # === 8- Lemmatizing
# lemmatizer = WordNetLemmatizer()
# lemmatized = np.array([])
# for l in filtered:
# 	lemmatized = np.append(lemmatized,lemmatizer.lemmatize(l))
# print(lemmatized)