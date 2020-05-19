# coding: utf8
#!/usr/bin/python3

# Tue 19 May 2020 10:29:01 CEST
# Author: Nicolas Flandrois

# Description: Training and discovery of Twitter API and Tweepy module
# https://tweepy.readthedocs.io/en/latest/

import os
from datetime import datetime as dt
import time
import tweepy

# 'Your Twitter API Key Here'
API_Key = os.environ.get('TWTR_API_KEY')
# 'Your Twitter API Secret Key Here'
API_Secret_Key = os.environ.get('TWTR_API_SECRET_KEY')

# 'Your Twitter AccessToken Here'
AccessToken = os.environ.get('TWTR_ACCESS_TOKEN')
# 'Your Twitter AccessTokenSecret Here'
AccessTokenSecret = os.environ.get('TWTR_ACCESS_TOKEN_SECRET')

auth = tweepy.OAuthHandler(API_Key, API_Secret_Key)
auth.set_access_token(AccessToken, AccessTokenSecret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()
print(user.screen_name)
print('\n')

# Follower = Accounts the follow this User
# for follower in tweepy.Cursor(api.followers).items():
#     if follower.name == 'Secrets d\'Histoire':
#         follower.follow()

# Friends = Accounts this user is following
# for friend in tweepy.Cursor(api.friends).items():
#     print(friend.name)
# """
# search = 'Python'
# nbTweets = 5

# for tweet in tweepy.Cursor(api.search, search).items(nbTweets):
#     try:
#         print('Tweet Liked')
#         tweet.favorite()
#         print('Tweet Retweeted')
#         tweet.retweet()
#         time.sleep(1)

#     except tweepy.TweepError as e:
#         print(e.reason)
#     except StopIteration:
#         print('Stop Iteration Exception Raised')
#         break
##############################################################
# id = '@Snubs'
# nbTweets = 1
# target_user = api.get_user(id)
# print(target_user.screen_name)
# print(target_user.name)
# print(target_user.description)
# print(target_user.location)
# tweet = target_user.status
# print(tweet.text)
# # tweet.retweet()
# tweet.favorite()
# # print(target_user)
#############################################################
# print(api.get_status('@Snubs'))
# ids = []
# for page in tweepy.Cursor(api.followers_ids, screen_name="GooldPearl").pages():
#     ids.extend(page)
#     # time.sleep(60)

# screen_names = [user.screen_name for user in api.lookup_users(user_ids=ids)]
# print(screen_names)
#############################################################################
usernames = ['@Snubs', '@HowtoADHD', '@mandyharvey', '@LindseyStirling',
             '@DalaiLama', '@terrycrews', '@dbwofficial']


while True:

    for username in usernames:
        print(f'\n\tTIME :\t{dt.now()}')
        target_user = api.get_user(username)

        screen_name = target_user.screen_name

        print('\n' + screen_name)
        print(target_user.name + '\n\n')

        tmpTweets = api.user_timeline(screen_name)

        for tweet in tmpTweets:

            print(f'- User {username} wrote\t:\t{tweet.text}')

            try:
                tweet.favorite()
                print('\t+ Liked')
                # tweet.retweet()
                # print('Retweeted')
            except:
                print('\t> Already added to favorites')

    print(f'\nTime :\t{dt.now()}\n\nScript is Sleeping! Zzzz...')
    time.sleep(45 * 60)
    print(f'\nTime :\t{dt.now()}\n\nFinished Sleeping... time to Work!\n\n')
