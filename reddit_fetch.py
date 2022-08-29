import praw
from config import config
from redvid import Downloader

def scrape(sub: str):
    reddit_p = praw.Reddit(
        client_id=config.reddit_client_id,
        client_secret=config.reddit_client_secret,
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36",
    )

    subreddit = reddit_p.subreddit(sub)

    reddit = Downloader(max_q=True)
    reddit.path = "assets"

    for i, submission in enumerate(subreddit.hot(limit=15)):
        if submission.over_18:
            continue
        if submission.is_video:
            try:
                reddit.url = submission.url
                reddit.download()
            except:
                print("error")
        else:
            continue