from classes.tweet_search import *
import data.mongo_setup as mongo_setup


def main():
    mongo_setup.global_init()
    main_tweet_search()
main()