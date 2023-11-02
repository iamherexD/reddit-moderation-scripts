import praw
import requests
import json
import time

reddit = praw.Reddit(
    client_id='YOUR_REDDIT_CLIENT_ID',
    client_secret='YOUR_REDDIT_CLIENT_SECRET',
    user_agent='YOUR_USER_AGENT',
)

discord_webhook_url = 'YOUR_DISCORD_WEBHOOK_URL'

subreddit_name = 'SUBREDDIT_NAME'

processed_post_ids = set()

def fetch_new_posts():
    subreddit = reddit.subreddit(subreddit_name)
    new_posts = subreddit.new(limit=5)

    for post in new_posts:
        if post.id not in processed_post_ids:
            payload = {
                'content': f'**New Post in r/{subreddit_name}**\n\n{post.title}\n{post.url}'
            }

            response = requests.post(discord_webhook_url, json=payload)

            if response.status_code != 204:
                print(f'Failed to send Discord webhook: {response.text}')

            processed_post_ids.add(post.id)

if __name__ == '__main__':
    while True:
        fetch_new_posts()
        time.sleep(5)
