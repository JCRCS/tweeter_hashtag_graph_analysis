#from classes.tweet_search import *
import data.mongo_setup as mongo_setup
# import classes.tweeter_hashtag_manager as tweeter_hashtag_manager
from classes.tweeter_hashtag_manager import *

def main():
    mongo_setup.global_init()
    my_tweeter_hashtag_manager = Tweeter_hashtag_manager()
    my_tweeter_hashtag_manager.run()
main()