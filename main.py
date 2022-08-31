import reddit_fetch
import os
import movie

for root, _, files in os.walk("assets"):
        for file in files:
            os.remove(os.path.join(root, file))

subreddits = ["videomemes", "shitposting", "funnyvideos", "doodoofart", "LaughterWorld", "dankvideos"]

for subreddit in subreddits:
    reddit_fetch.scrape(subreddit)

videos = list()

for root, _, files in os.walk("assets"):
        for file in files:
            videos.append(f"{root}/{file}")

movie.concatenate(videos, "out.mp4")
os.remove("out.mp4")