import praw
import time


r= praw.Reddit(username="FMFbootbot",
			   password="minami",
			   client_id="TvMQyCMAKBrnPw",
			   client_secret="a_PEj5ShxAUtOgpppPTXSP3hWRE",
			   user_agent="FMF bot by /u/cropic")


words_to_match=['red wing ','boots','wolverine','beckmans']

cache=[]

def run_bot():
	subreddit=r.subreddit("frugalmalefashion")

	

	for comment in subreddit.comments(limit=25):
		comment_text=comment.body.lower()

		isMatch=any(string in comment_text for string in words_to_match)

		if comment.id not in cache and isMatch:
			comment.reply('Hi, I\'m FMF boot bot . Check out this boot inspiration album. http://imgur.com/a/fwSDr')
			cache.append(comment.id)




while True:
	run_bot()
	time.sleep(10)






