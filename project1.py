import tweepy
import sys
import time
#mainmanu
while True:
	print("1.Retrieve Tweets")
	print("2.Count the followers")
	print("3.Determine the sentiment")
	print("4.Determine location,language and time zone.")
	print("5.Compare tweets ")
	print("6.Analyze top usage ")
	print("7.Tweet a message")
	print("8.exit")
	choice=int(input("enter any choice"))
	consumer_key='7NhN783A9iMqWLxU5NL6yIa29'
	consumer_secret='kdlWCNKdO94wJ0yoWiKkrqo21JOx8eJGjba4epCUB1a9rWgbvE'
	access_token='1011138700347105280-WsH7oXzs53sat5c1vaB3GYahm3sdGj'
	access_token_secret='RI02aleBGhf7O2oTOUbzGCNvc9WmVG0obmmpKBV9ODh3L'
	auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
	auth.set_access_token(access_token,access_token_secret)
	api=tweepy.API(auth)
	def first():
		user_search=input("enter any hash tag search: ")
		tweets=api.search(user_search,lang="en",count=5,tweet_mode="extended")
		#print(tweets)
		for tweet in tweets:
			print("--------------")
			print(tweet.full_text)
			print("--------------")
	def second():
		user_id=input("enter any id to count the follower:" )
		user=api.get_user(user_id)
		print(user.screen_name)
		print(user.friends_count)
		return
	def thrird():
		status=input("enter any status")
		user_id=input("enter any id to upload the status:")
		api.update_status(status,user_id)
	def fourth():
		user_id = input("enter the any id to see location:")
		user = api.get_user(user_id)
		print("location:",user.location)
		print("time_zone:",user.time_zone)
		print("language:",user.langs)
	def fiveth():
		user_id=input("enter the id to send message:")
		message=input("enter any massage:")
		api.send_direct_message(user=user_id,text=message)
	def sixth():
		auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_token,access_token_secret)
		api = tweepy.API(auth)
		username=input("enter any user id:")
		tweets = api.user_timeline(screenname=username, count=20)
		tmp = []
		tweets_for_csv = [tweet.text for tweet in tweets]
		for j in tweets_for_csv:
			tmp.append(j)
		flotpos = 0
		flotneg = 0
		flotneu = 0
		print(tmp)
		from paralleldots import set_api_key,get_api_key,sentiment
		set_api_key("60TE8tX8lV1KIy8OhpGEUpLRa4RvyJaXA7IsIEXt6x4")
		get_api_key()
		for  t in tmp:
			a = sentiment(t)
			if a['sentiment'] == 'positive':
				flotpos += 1
			if a['sentiment'] == 'negative':
				flotneg+= 1
			if a['sentiment'] == 'neutral':
				flotneu+= 1
		if (flotpos > flotneg) and (flotpos > flotneu):
				print("postive")
		if (flotneg > flotneu) and (flotneg > flotpos):
				print("negative")
		if (flotneu > flotneg) and (flotneu > flotpos):
					print("neutral")
	def seventh():
			user_id = input("enter 1st id Count the compare:")
			user = api.get_user(user_id)
			a1= user.followers_count
			user_id1 = input("enter 2nd id to compare:")
			user1 = api.get_user(user_id1)
			a2 = user1.followers_count
			if a1>a2:
				print("{} is the best user of twitter".format(user.name))
			else:
				print("{} is the best user of tweeter".format(user1.name))
	if choice==1:
		first()
	if choice==2:
		second()
	if choice==3:
		thrird()
	if choice==4:
		fourth()
	if choice==5:
		fiveth()
	if choice==6:
		sixth()
	if choice==7:
		seventh()
	if choice==8:
		exit()