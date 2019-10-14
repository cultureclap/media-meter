from keys import cultureclap as cck

import tweepy
from pprint import pprint as ppr




# tname = sys.argv[1]
# t_user = TweetUser.objects.filter(handle=tname)[0]
# print(t_user)

def trypass(test):
	try:
		item = test
	except:
		item = 'nada'
	print(item)
	return item

t_user = cck

auth = tweepy.OAuthHandler(t_user['token'], t_user['token_key'])
auth.set_access_token(t_user['secret'], t_user['secret_key'])
api = tweepy.API(auth)

sn = api.get_user('duckduckgo')

# ppr(sn._json)

print('Name', sn.name)
print('Screen Name', sn.screen_name)
print('Favorites', sn.favourites_count)
print('Followers', sn.followers_count)
print('Following', sn.friends_count)

newtl = api.user_timeline('duckduckgo', count=20)

for tw in newtl[:10]:
	text = tw.text
	if not text.startswith("RT"):
		tweet = {}
		tweet['text'] = tw.text
		tweet['links'] = tw.entities['urls']
		tweet['hashtags'] = tw.entities['hashtags']
		tweet['user_mentions'] = tw.entities['user_mentions']
		tweet['fave_count'] = tw.favorite_count
		tweet['rt_count'] = tw.retweet_count
		tweet['twid'] = tw.id
		tweet['tw_datetime'] = tw.created_at
		ppr(tweet)
		print( '\n\n\n ++++ \n\n\n')

# ppr(newtl[3]._json)