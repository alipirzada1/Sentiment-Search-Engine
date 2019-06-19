# import nltk 
# from nltk.corpus import sentiwordnet as swn 
# from nltk.stem import WordNetLemmatizer

# print(swn.senti_synset('breakdown.n.03'))
# print(list(swn.senti_synsets('slow')))

# lemmatizer = WordNetLemmatizer()

# word = lemmatizer.lemmatize(word)

# word = 'hate'

# word = swn.senti_synsets(word)

# word = list(word)[0]

# print(word.neg_score())

# # === Code For finding polarity (pos/neg) score of a word given in the corpus 
# score = list(swn.senti_synsets(word,'n'))[0].neg_score()
# score = list(swn.senti_synsets(word,'n'))[0].pos_score()

# ========================================

# ========================================

# from textblob import TextBlob
# #  Sentiment Using TextBlob Naive Bayse algorithm inside 
# txt = TextBlob("this is a good cellphone")
# print(txt.tags)
# print(txt.noun_phrases)
# print(txt.sentiment)
# print(txt.sentiment.polarity)

# print('=================')
# print(txt)
# print(filtered)
# print(checkarr)