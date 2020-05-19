# coding: utf8
#!/usr/bin/python3

# Author: Nicolas Flandrois
# Date: Sunday, March 29rd, 2020
# https://tweepy.readthedocs.io/en/latest/

# Description: Bot using twitter API, given a list of "Friends' id" on Twitter,
# it will automatically 'like' their 20 latest tweets, and send an email to tell
# the user it's done a good job.
# This version is ready to be used in a CRONTAB schedule.

import os
import smtplib
from email.message import EmailMessage
from datetime import datetime as dt
import tweepy

print(f'\nTime :\t{dt.now()}\n\nTwitter Script starting. Please wait.')


def send_email(from_addr, gmail_key,
               to_addrs, subject,
               body_txt='DEFAULT - This is a plain text email',
               body_html=None, attached_file=None):
    try:
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = from_addr
        msg['To'] = to_addrs

        msg.set_content(body_txt)  # Body as text

        if body_html is not None:
            msg.add_alternative(body_html, subtype='html')  # Body as HTML

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(from_addr, gmail_key)
            smtp.send_message(msg)
            print('Email sent successfully')

    except Exception as e:
        print(e)
        print('\nEmail failed to send.')


def twtr_like_bot(API_Key, API_Secret_Key, AccessToken, AccessTokenSecret, usernames_list):
    auth = tweepy.OAuthHandler(API_Key, API_Secret_Key)
    auth.set_access_token(AccessToken, AccessTokenSecret)

    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)

    # user = api.me()
    # print(user.screen_name)

    for username in usernames_list:
        tmpTweets = api.user_timeline(
            screen_name=username)

        for tweet in tmpTweets:
            try:
                # print(tweet.text)
                tweet.favorite()
                # tweet.retweet()
            except:
                pass

    # print(f'\nTime :\t{dt.now()}\n\nTwitter Script Finished.')
    return True


# Twitter Variables
API_Key = os.environ.get('TWTR_API_KEY')
API_Secret_Key = os.environ.get('TWTR_API_SECRET_KEY')

AccessToken = os.environ.get('TWTR_ACCESS_TOKEN')
AccessTokenSecret = os.environ.get('TWTR_ACCESS_TOKEN_SECRET')

# Update/Modify/Customize your list of 'friends' here.
usernames_list = ['@Snubs', '@HowtoADHD', '@mandyharvey', '@LindseyStirling']

# Email Variables
from_addr = os.environ.get('EMAIL_USER')
gmail_key = os.environ.get('EMAIL_PASS')

to_addrs = from_addr

# Succeed
subject_success = f'Twitter Bot - SUCCESS - \
{dt.now().strftime("%A, %d. %B %Y %I:%M%p")}'

msg_success = f"""This email was automatically sent by your Twitter bot.
Your Twitter Account Successfully liked your favorit twitter-friends.
{dt.now().strftime("%A, %d. %B %Y %I:%M%p")}
"""

body_html_success = f"""<!DOCTYPE html>
<html>
    <body>
        <h1 style="color:SlateGray;">Your Twitter Account Successfully liked your favorit twitter-friends.</h1>
        <p>This email was automatically sent by your Twitter bot.</p>
        <p>Your Twitter-bot is setup to like the last 20 tweets not liked yet, from each friend's account in your list.</p>
        <p>The Twitter bot last worked on {dt.now().strftime("%A, %d. %B %Y %I:%M%p")}.</p>
    </body>
</html>"""

# Failed
subject_failed = f'Twitter Bot - FAILED - \
{dt.now().strftime("%A, %d. %B %Y %I:%M%p")}'

msg_failed = f"""This email was automatically sent by your Twitter bot.
Your Twitter Account failed to like your favorit twitter-friends.
{dt.now().strftime("%A, %d. %B %Y %I:%M%p")}
"""

body_html_failed = f"""<!DOCTYPE html>
<html>
    <body>
        <h1 style="color:SlateGray;">Your Twitter Account <b>FAILED</b> to like your favorit twitter-friends.</h1>
        <p>This email was automatically sent by your Twitter bot.</p>
        <p>The Twitter bot last worked on {dt.now().strftime("%A, %d. %B %Y %I:%M%p")}.</p>
    </body>
</html>"""

if __name__ == "__main__":

    if twtr_like_bot(API_Key, API_Secret_Key, AccessToken,
                     AccessTokenSecret, usernames_list) is True:

        send_email(from_addr, gmail_key, to_addrs,
                   subject_success, msg_success, body_html_success)
    else:
        send_email(from_addr, gmail_key, to_addrs,
                   subject_failed, msg_failed, body_html_failed)
