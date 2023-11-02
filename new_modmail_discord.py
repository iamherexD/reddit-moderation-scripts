import praw
import requests
import json

reddit_client_id = 'YOUR_REDDIT_CLIENT_ID'
reddit_client_secret = 'YOUR_REDDIT_CLIENT_SECRET'
reddit_username = 'YOUR_REDDIT_USERNAME'
reddit_password = 'YOUR_REDDIT_PASSWORD'
reddit_user_agent = 'YOUR_REDDIT_USER_AGENT'

discord_webhook_url = 'YOUR_DISCORD_WEBHOOK_URL'

reddit = praw.Reddit(
    client_id=reddit_client_id,
    client_secret=reddit_client_secret,
    username=reddit_username,
    password=reddit_password,
    user_agent=reddit_user_agent
)

modmail_subreddit = reddit.subreddit('YOUR_MODMAIL_SUBREDDIT')

for message in modmail_subreddit.mod.stream_modmail():
    if message.__class__.__name__ == 'ModmailMessage':
        modmail_link = f"https://www.reddit.com{message.permalink}"
        modmail_content = message.body
        modmail_sender = message.author.name

        discord_message = f"**New Modmail Message**\n\n" \
                          f"Sender: {modmail_sender}\n\n" \
                          f"Content: {modmail_content}\n\n" \
                          f"[View Modmail]({modmail_link})"

        payload = {
            'content': discord_message
        }
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post(discord_webhook_url, data=json.dumps(payload), headers=headers)

        if response.status_code != 200:
            print(f"Failed to send the message to Discord. Status code: {response.status_code}")
