import time
import tweepy
import utils
from authenticate import Auth
api = Auth()



ids = []
for page in tweepy.Cursor(api.followers_ids, screen_name="paleshadow7").pages():
    ids.extend(page)

ids = [str(i) for i in ids]
f = open("save.txt", "w")
f.write('\n'.join(ids))
