import twitter

def getpost_clean(user,c_key,c_secret,a_key,a_secret):
	api = twitter.Api(consumer_key=c_key, consumer_secret=c_secret, access_token_key=a_key, access_token_secret=a_secret)	
	statuses = api.GetUserTimeline(user)
	return [s.text for s in statuses]	
def getpost(user):
	api = twitter.Api(consumer_key=c_key, consumer_secret=c_secret, access_token_key=a_key, access_token_secret=a_secret)	
	statuses = api.GetUserTimeline()
	return statuses
def getfriends(user):
	userems = api.GetFriends(user)
	return userems
	#print [u.name for u in users]
def twitterx(input,ck,cs,ak,asx):
	api = twitter.Api(consumer_key=c_key, consumer_secret=c_secret, access_token_key=a_key, access_token_secret=a_secret)	
	user = input
	x = getpost_clean(user,ck,cs,ak,asx)
	link1 = "http://twitter.com/"
	link2 = link1+user
	sayer = 'Latest Tweet: "'+x[0]+'" ['+link2+']'
	return sayer