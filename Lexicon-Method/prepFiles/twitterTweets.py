# import tweepy
# import json
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

# tweets = tweepy.Cursor(api.search,	q='obama -filter:retweets',	lang='en').items(100)

# for loop in tweets:
# 	if not 'RT @' in loop.text:
# 		print(loop.text,'\n\n')

# # ==================
# # Another Method
# # ==================

# for x in range(50):
# 	for loop,loop2 in zip(word_list,file_list):
# 		tweets = api.search(loop)
# 		filehandle = open(loop2,'a')
		
# 		for list in tweets:
# 			txt = str(list.created_at) + "     " + str(list.text)
# 			txt = txt.encode('ascii','ignore').decode('ascii')
# 			filehandle.write(txt + "\n")
# 			time.sleep(1)
# 		filehandle.close()
# 		time.sleep(2)