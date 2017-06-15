import os
import tweepy
from tweepy import OAuthHandler


def Auth():
    consumer_key = 'nWFOYiDwURNw8hvety2UXgxg9'
    consumer_secret = 'trb3NETdthh6Ymr4SkH7F8g1Rqhm4HBFCgSKdeBstAPv36L0QK'
    access_token = '871120857577525248-uToYqbCL9u29x99OsAMYH93FnzpSZnw'
    access_secret = 'MApnpeCpYOXHTTN9ZJidly9O1CLUriN0yPTTl5gAVsk2H'

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    return tweepy.API(auth, wait_on_rate_limit=True)


def GetNames(api, ids):
    h = int(len(ids)/100)

    users = []
    for i in range(h):
        screen_names = [user.screen_name for user in api.lookup_users(user_ids=ids[i*100:i*100+100])]
        users += screen_names

    users += [user.screen_name for user in api.lookup_users(user_ids=ids[h*100:])]

    return users


def WriteFollowerIDs(api, user_id):
    fName = "ids/{}".format(user_id)
    if os.path.isfile(fName):
        print("File already exists for {}".format(user_id))
        return False

    ids = []
    for page in tweepy.Cursor(api.followers_ids, id=user_id).pages(150):
        ids.extend(page)

    ids = [str(i) for i in ids]
    f = open(fName, "w")
    f.write('\n'.join(ids))
    f.close()

    return True
