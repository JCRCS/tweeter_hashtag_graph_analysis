#from classes.tweet_search import *
import data.mongo_setup as mongo_setup
import classes.tweet_hashtag_fetcher as fetcher


def main():
    mongo_setup.global_init()
    fetch = fetcher.Tweet_hastag_fetcher()
    fetch.run()
    #main_tweet_search()
main()