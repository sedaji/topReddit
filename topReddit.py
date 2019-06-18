#!/usr/bin/python3
import praw
import sys
from praw.models import MoreComments

'''By default, this program returns TOP 3 posts/comments of subreddit learnprogramming.
It can take up to 3 arguments. 
argv[1] = name of subreddit
argv[2] = length of time, ie. day, month, all. 
argv[3] = number of posts

Example: ./topReddit.py askreddit month 5
Will return TOP 5 posts from r/askreddit in the past month.'''

# Create the Reddit instance and log in
defSubreddit = 'learnprogramming'
reddit = praw.Reddit('bot1') # bot1 is defined in a seperate file 'praw.ini'
counter = 1
scope = 'day'
numberofposts = 3

# Settings for argv 
if len(sys.argv) > 1:
    defSubreddit = (sys.argv[1])
if len(sys.argv) > 2:
    scope = (sys.argv[2])
if len(sys.argv) > 3:
    numberofposts = int(sys.argv[3])
subr = reddit.subreddit(defSubreddit)

def redpost():
    counter = 1
    for submission in subr.top(scope,limit=numberofposts): # For total posts, iterate through each post
        print(' +' * 51, "\n")
        print(f"[POST {counter}]".center(100,' '),end='\n\n')
        print("\treddit.com"+submission.permalink,end='\n\n')
        print("\t[Title]:", submission.title)
        print("\t[/u/",end='') # START DIY solution to format since praw formatting adds a space
        print(submission.author,end='')
        print(" +",end='')
        print(submission.score,end='] ')# END DIY solution
        print("\n\t[Text]:", submission.selftext,"\n")
        print("[COMMENTS]".center(100,' '),end='\n\n')
        submission.comment_sort = 'best'
        submission.comment_limit = 3
        for top_level_comment in submission.comments: # For each post, iterate through each comment
            if isinstance(top_level_comment, MoreComments): # Handles common praw error when fetching comments
                continue              
            print("\t[/u/",end='')
            print(top_level_comment.author,end='')
            print(" +",end='')
            print(top_level_comment.score,end=']: ')
            print(top_level_comment.body,end='\n\n')      
        counter += 1  
redpost()

#script for user comments
# user = reddit.redditor('sedaji')
# for comment in user.comments.new(limit=10):
#     print(str(counter)+'. '+comment.body)
#     print('~' * 100)
#     counter += 1
