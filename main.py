import reddit_fetch
import os
import movie

for root, _, files in os.walk("assets"):
        for file in files:
            os.remove(os.path.join(root, file))

reddit_fetch.scrape("videomemes")
reddit_fetch.scrape("shitposting")
reddit_fetch.scrape("funnyvideos")
reddit_fetch.scrape("doodoofart")
reddit_fetch.scrape("LaughterWorld")

videos = list()

for root, _, files in os.walk("assets"):
        for file in files:
            videos.append(f"{root}/{file}")

movie.concatenate(videos, "out.mp4")