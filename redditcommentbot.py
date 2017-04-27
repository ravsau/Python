import praw
import time


r= praw.Reddit(username="yourusername",
			   password="yourpass",
			   client_id="TvMQyCMAKBrnPw",
			   client_secret="yoursecret",
			   user_agent="FMF bot by u/you")


words_to_match=['red wing ','boots','wolverine','beckmans']


cache1=[]
cache=[]

def run_bot():
	ids  = open('post.txt', 'r+')
	a=ids.read()
	
	print (a)

	

	

	

	for submission in r.subreddit('frugalmalefashion').new():
		sub_text=submission.title.lower()

		isMatch=any(string in sub_text for string in words_to_match)

		if submission.id not in a and isMatch:
			submission.reply('Hi, I\'m FMF boot bot . Check out this boot inspiration album. http://imgur.com/a/fwSDr \n \
				#Red Wing Inspiration Album: http://imgur.com/a/lJYIb \n \
				#')
			ids.write(submission.id +" ") 
			
	ids.close()		




		



while True:
	run_bot()
	time.sleep(1)






