import datetime
import bson
from typing import List
import pandas as pd
import re

 
from data.graph import Graph
from data.hashtag import Hashtag
from data.space import Space
from data.tweet import Tweet

class Data_service():
    def __init__(self):
        pass
    def register_tweet(self, tweet_id, tweet_date, author_info, hashtag, symbols, user_mensions, urls, retweet, text:str) -> Tweet:
        """add a type to a entity
            args*:
                tweet_id: str
                tweet_date: DateTime
                author_info: {}
                hashtag: []
                symbols: []
                user_mensions: []
                urls: []
                retweet: Int 
                text: str
            return:
                tweet
                    return the registered tweet
        """

        tweet = Tweet()

        tweet.tweet_id = tweet_id
        tweet.tweet_date = tweet_date
        tweet.author_info = author_info
        tweet.hashtag = hashtag
        tweet.symbols = symbols
        tweet.urls = urls
        tweet.retweet = retweet
        tweet.hastags = []
        tweet.user_mensions = user_mensions
        tweet.text = text
        tweet.save()    
        #entity = Entity.objects(id = entity.id).first()
        # entity.typeObj_ids.append(typeObj.id)
        # entity.save()

        return tweet