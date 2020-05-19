# coding: utf8
#!/usr/bin/python3

# Tue 19 May 2020 10:29:01 CEST
# Author: Nicolas Flandrois

# ***Description***: Using Twitter API, this short script will output text files,
# listing who is following whom.

import os
from datetime import datetime as dt
import tweepy


def twtr_following_bot(API_Key, API_Secret_Key, AccessToken, AccessTokenSecret):
    """This simple twitter bot will automatically extract all the friends this
    account is following, and output them in a list in a text file.

    >>> Who Am I Following?

    Takes Arguments (given by twitter API for your own Account):
        API_Key,
        API_Secret_Key,
        AccessToken,
        AccessTokenSecret"""

    auth = tweepy.OAuthHandler(API_Key, API_Secret_Key)
    auth.set_access_token(AccessToken, AccessTokenSecret)

    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)

    # user = api.me()
    # print(user.screen_name)
    follow_list = []

    for friend in tweepy.Cursor(api.friends).items():
        follow_list.append(f'{friend.name}\t\t@{friend.screen_name}\n\n')

    follow_str = ''.join(follow_list)

    with open("FollowingOnTwitterList.txt", "w") as f:
        f.write(f'{dt.now()}\n\n{follow_str}')


def twtr_followers_bot(API_Key, API_Secret_Key, AccessToken, AccessTokenSecret):
    """This simple twitter bot will automatically extract all those following your
    twitter account, and output them in a list in a text file.

    >>> Who is Following Me?

    Takes Arguments (given by twitter API for your own Account):
        API_Key,
        API_Secret_Key,
        AccessToken,
        AccessTokenSecret"""

    auth = tweepy.OAuthHandler(API_Key, API_Secret_Key)
    auth.set_access_token(AccessToken, AccessTokenSecret)

    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)

    # user = api.me()
    # print(user.screen_name)
    follow_list = []

    for follower in tweepy.Cursor(api.followers).items():
        follow_list.append(f'{follower.name}\t\t@{follower.screen_name}\n\n')

    follow_str = ''.join(follow_list)

    with open("FollowersOnTwitterList.txt", "w") as f:
        f.write(f'{dt.now()}\n\n{follow_str}')


##############################################################################

API_Key = os.environ.get('TWTR_API_KEY')
API_Secret_Key = os.environ.get('TWTR_API_SECRET_KEY')

AccessToken = os.environ.get('TWTR_ACCESS_TOKEN')
AccessTokenSecret = os.environ.get('TWTR_ACCESS_TOKEN_SECRET')

if __name__ == "__main__":

    twtr_followers_bot(API_Key, API_Secret_Key, AccessToken,
                       AccessTokenSecret)

    twtr_following_bot(API_Key, API_Secret_Key, AccessToken,
                       AccessTokenSecret)
