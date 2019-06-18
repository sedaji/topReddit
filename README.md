# topReddit

Before downloading and executing this program, log into http://reddit.com

Go to https://www.reddit.com/prefs/apps/

Type in any name, choose script, reddit.com for redirect uri. Submit.

Save the Client ID And Client SECRET.

Put these in the praw.ini file.

# What this program does: 

By default, this program returns TOP 3 posts & comments of subreddit learnprogramming.
It can take up to 3 arguments. 

argv[1] = name of subreddit

argv[2] = length of time, ie. day, month, all. 

argv[3] = Number of posts

Example: ./topReddit.py askreddit month 5

Will return TOP 5 posts from r/askreddit in the past month.

# Default OUTPUT:

![Image](https://raw.githubusercontent.com/sedaji/topReddit/master/Annotation%202019-06-18%20143308.png)
