import praw

reddit = praw.Reddit(
    client_id='YOUR_CLIENT_ID',
    client_secret='YOUR_CLIENT_SECRET',
    user_agent='YOUR_USER_AGENT',
    username='YOUR_USERNAME',
    password='YOUR_PASSWORD'
)

subreddit_name = 'YOUR_SUBREDDIT_NAME'
subreddit = reddit.subreddit(subreddit_name)

modqueue = subreddit.mod.modqueue()

for item in modqueue:
    if isinstance(item, praw.models.Submission):
        item.mod.remove(spam=True)

print("Modqueue cleaning complete!")
