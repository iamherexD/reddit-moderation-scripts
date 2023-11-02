# Auto remove NSFW posts and log the permalinks to discord

import praw
import requests
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

discord_webhook_url = 'WEBHOOK_URL'

reddit = praw.Reddit(
    client_id='CLIENT_ID',
    client_secret='CLIENT_SECRET',
    user_agent='USER_AGENT',
    username='REDDIT_USERNAME',
    password='REDDIT_PASSWORD'
)

subreddit_name = 'SUBREDDIT_NAME'

subreddit = reddit.subreddit(subreddit_name)

def log_to_discord(submission):
    permalink = 'https://reddit.com' + submission.permalink 
    payload = {
        'content': 'NSFW Post Removed',
        'embeds': [
            {
                'title': 'NSFW Post Removed',
                'description': submission.title,
                'fields': [
                    {'name': 'Permalink', 'value': permalink, 'inline': False}
                ],
            }
        ]
    }
    response = requests.post(discord_webhook_url, json=payload)
    if response.status_code != 204:
        logging.error(f'Failed to log to Discord: {response.text}')

while True:
    try:
        for submission in subreddit.stream.submissions():
            if submission.over_18:
                submission.mod.remove()
                logging.info('Removed NSFW post: {}'.format(submission.title))

                log_to_discord(submission)

    except Exception as e:
        logging.error('An error occurred: {}'.format(str(e)))
