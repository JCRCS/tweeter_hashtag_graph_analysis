# import service.data_service as data_svc
# import classes.tweet_hashtag_fetcher as tweet_fetcher

from service.data_service import *
from classes.tweet_hashtag_fetcher import *


class Space_Manager():
    """ 
    Manage the spaces and the tweets inside of each space
    to fill the spaces with different tweeter searches
    """
    def __init__(self):
        self.data_svc = Data_service()
        space = self.set_space(name= "gt")
        self.tweet_fetcher = Tweet_hastag_fetcher(space= space)

    def run(self):
        #fetch.run()
        self.tweet_fetcher.one_run()
        #main_tweet_search()
        print("Space_manager")
    
    def set_space(self, name = ""):
        """ 
        to get the specific space due to the space_name
            *args:
                space_name: str
            return:
                space: Space
                    return the space that match with the
                    space_name
        """
        space = self.data_svc.register_space(name)
        return space
    
    def get_hashtags_relations(self, tweet):
        """ 
        this method return the hashtags relations of 
        each tweet in a specific space
            *args:
                # space: Space
                tweet: Tweet
            return:
                array
        """
        hashtag_nodes = tweet.hashtag_nodes
        return list(hashtag_nodes)
    
    def get_tweets(self, space):
        """ 
        give the tweeters of the specified space
            *args:
                space
            return:
                tweeters: List(Tweet)
        """
        tweets = self.data_svc.get_tweets(space = space)
        return tweets
    