import praw
import requests
import json

reddit_client_id = 'your_client_id'
reddit_client_secret = 'your_client_secret'
reddit_user_agent = 'your_user_agent'
reddit_username = 'your_bot_username'
reddit_password = 'your_bot_password'

slack_webhook_url = 'https://hooks.slack.com/services/your/webhook/url'

reddit = praw.Reddit(
    client_id=reddit_client_id,
    client_secret=reddit_client_secret,
    user_agent=reddit_user_agent,
    username=reddit_username,
    password=reddit_password
)

subreddit = reddit.subreddit('subreddit_name')
slack_channel = 'slack_channel'

modmail_subject = 'This is the subject of the modmail'
modmail_body = 'This is the body of the modmail.'

modmail = subreddit.message('r/' + subreddit.display_name, modmail_subject, modmail_body)

slack_message = {
    "text": f"New modmail from r/{subreddit.display_name}:\nSubject: {modmail_subject}\nMessage: {modmail_body}"
}

response = requests.post(slack_webhook_url, data=json.dumps(slack_message),
                        headers={'Content-Type': 'application/json'})

if response.status_code == 200:
    print('Modmail sent to Slack successfully')
else:
    print('Failed to send modmail to Slack')
