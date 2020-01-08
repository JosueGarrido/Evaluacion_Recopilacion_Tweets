import pymongo
from pymongo import MongoClient
import json
import twitter
from pprint import pprint

CONSUMER_KEY="HvCg23VwyIGwnVe5krvHKuZGO"
CONSUMER_SECRET="KUwAEDDqogw0xlHr1LQiaECD4q42gpFRPkUS0NLHZm51Y9gMRF"
OAUTH_TOKEN="115946548-x5JL2LFNp26y2t0WlBvQE7GirkGeNZUaYLUM1GGL"
OAUTH_TOKEN_SECRET="ul2Q4nw9112ATj4iyFu2VIj12IElGb0GRIr3wBnBPxBAE"


auth=twitter.oauth.OAuth(OAUTH_TOKEN,OAUTH_TOKEN_SECRET,CONSUMER_KEY,CONSUMER_SECRET)
twitter.api=twitter.Twitter(auth=auth)

client=MongoClient()
db=client.tweet_db
tweet_collection=db.tweet_collection
tweet_collection.create_index([("id",pymongo.ASCENDING)],unique=True)

count=1000
q="Vans"
search_results=twitter.api.search.tweets(count=count,q=q)
#pprint(search_results['search_metadata'])

statuses=search_results["statuses"]
since_id_new=statuses[-1]['id']
for statues in statuses:
    try:
        tweet_collection.insert(statues)
    except:
        pass
    
tweet_cursor=tweet_collection.find()
print(tweet_cursor.count())
user_cursor=tweet_collection.distinct("user.id")
print(len(user_cursor))
for document in tweet_cursor:
    try:
        print('-----')
        print('name:-',document["user"]["name"])
        print('text:-',document["text"])
        print('Created Date:-',document["created_at"])
    except:
        print("Error in Encoding")
        pass
