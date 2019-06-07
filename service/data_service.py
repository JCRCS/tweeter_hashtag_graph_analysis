import datetime
import bson
from typing import List
import pandas as pd
import re

 
from data.graph import Graph
from data.hashtag import Hashtag
from data.space import Space
from data.tweet import Tweet




def register_tweet(tweet_id, tweet_date, author_info, hashtag, symbols, user_mensions, urls, retweet, text:str) -> Tweet:
    """add a type to a entity
        args*:
            entity: Entity
                the Entity where will be stored the typeObj
            typeObjUri: str
                the typeObj URI to register into the Entity
        return:
            typeObj
                return the typeObj registered
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