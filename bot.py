import praw
import pdb
import re
import os
import random

def login():
	r = praw.Reddit(
		username=os.environ['username'],
		password=os.environ['password'],
		client_id=os.environ['client_id'],
		client_secret=os.environ['client_secret'],
		user_agent="Jon Snow Bot v0	.1"
		)
	return r

John_snow_dialogues=["She's mah queen","I duhn't wan' it","**yells at dragon**"]

reddit = login()
subreddit=reddit.subreddit("freefolk")

for submission in subreddit.stream.submissions():
	if re.search("snow", submission.title,re.IGNORECASE):
		bot_reply=random.choice(John_snow_dialogues)
		submission.reply(bot_reply)
		print("Bot replied to: ",submission.title)

for comment in subreddit.stream.comments():
	if re.search("snow",comment.body,re.IGNORECASE):
		bot_reply=random.choice(John_snow_dialogues)
		comment.reply(bot_reply)
