import time
import csv
import datetime
from datetime import datetime, timedelta

#import service.data_service as data_svc

from service.data_service import *

class Node_maker_hashtag():
    def __init__(self):
        self.data_svc = Data_service()   

    def run(self, space:Space):  
        print("node_maker_hashtag")
        
    
    # def create_hashtag_nodes(self, space):
    #     """ create notes from the hashtags of the tweeters,
    #         also put into the tweeters the ids of the hashtag nodes 
    #         from one single space
    #         *args:
    #             space: Space
    #         return
    #             hashtags: List(Node)
    #     """
    #     node_type = self.data_svc.register_node_type("hashtag")
    #     tweets = self.data_svc.get_tweets(space= space)
    #     for iTweet in tweets:
    #         self.create_hashtag_node(iTweet,node_type)


    # def create_hashtag_node(self, tweet: Tweet, node_type: Node_type):
    #     """ create notes from the hashtags of the tweeters,
    #         also put into the tweeters the ids of the hashtag nodes 
    #         *args:
    #             tweeters: List(Tweet
    #             node_type: Node_type
    #         return
    #             hashtags: List(Node)
    #     """
    #     try:
    #         hashtags = tweet.hashtag
    #     except:
    #         print("there isn't hashtags")
    #     for iHashtag in hashtags:
    #         node = self.data_svc.register_node(name =  iHashtag["text"], node_type = node_type )
    #         self.data_svc.register_hashtag_tweet(node, tweet)


        
        
        
