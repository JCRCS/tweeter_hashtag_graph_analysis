import tweepy
import time
import csv
import datetime
from datetime import timedelta

# import service.data_service as data_svc
from service.data_service import *

class Tweet_hastag_fetcher():
    def __init__(self, space = None):
        self.data_svc = Data_service()
        self.tweeter_api = self.tweeter_init()
        searched_tweets = [] 
        self.space = space
        pass
    

    def run(self):  
        print("hello_world")
        self.periodic_work_cursor(30)

    def one_run(self):  
        print("test fetcher (one_work)")
        self.one_work_cursor(5)
        
        
        


    def tweeter_init(self):
        # twitter setup
        consumer_key = "3cSaGgMXZGNtHw2nGMzS67oZ0"
        consumer_secret = "uK2Ny7rD0RYmjku54LVpRjxG6EPMGYKmzkHAze1XT1OgpDHDEf"
        access_token = "933397205985218570-stOqCQwrfaj66WdxKZxWaPtu7SVjPqJ"
        access_token_secret = "STPtNp6QhwGylbuFYd73UXQ7FT6GYSWYcr6GdUMHJnBQ8"
        # Auth
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth) 
        return api

    def normalize_timestamp(self, time):
        mytime = datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
        mytime += timedelta(hours=1)   # the tweets are timestamped in GMT timezone, while I am in +1 timezone
        return (mytime.strftime("%Y-%m-%d %H_%M_%S")) 

    def periodic_work_cursor(self, interval = 30):
        work_space = '.\\storage\\'
        file_name = work_space+'tweet'+str(datetime.datetime.now().strftime("%Y-%m-%d %H_%M_%S"))
        last_id = 0
        fetch_count = 0
        while True:
            last_id = self.get_twitter_data_cursor(last_id = last_id, since_date= "2019-06-7", file_name= file_name)
            time.sleep(interval)
            fetch_count += 1
            print("fetch count: ", fetch_count)
    
    def one_work_cursor(self, interval = 30):
        work_space = '.\\storage\\'
        file_name = work_space+'tweet'+str(datetime.datetime.now().strftime("%Y-%m-%d %H_%M_%S"))
        last_id = 0
        fetch_count = 0
        #get max tweet id 
        # get min tweet id 
        #
        last_id = self.get_twitter_data_cursor(last_id = last_id, since_date= "2019-06-9", file_name= file_name)
        time.sleep(interval)
        fetch_count += 1
        print("fetch count: ", fetch_count)

    # get data every couple of minutes
    def get_twitter_data_cursor(self, last_id = -1, since_date = "2019-06-07", file_name = "tweet_aux"):
        since_date = since_date
        last_id = last_id
        query = "guatemala"
        max_tweets = 10
        max_id = 0
        searched_tweets = []
        print(str(datetime.datetime.now()))
        csvFile = open(file_name+'.csv', 'a', newline = '')
        #Use csv Writer
        csvWriter = csv.writer(csvFile)
    #     while True:#len(searched_tweets) < max_tweets:
            #count = max_tweets - len(searched_tweets)
        print("last_id: ",str(last_id))
        try:
            new_tweets = tweepy.Cursor(self.tweeter_api.search,
                            tweet_mode='extended',
                            q=query,
                            count=max_tweets,
                            lang = "es",
                            since= since_date,
                            max_id = str(last_id)).items()
            # if not new_tweets:
            #     print ("not founded")
            searched_tweets = new_tweets
            
            #print("finished", new_tweets)#searched_tweets)
        except tweepy.TweepError as e:
            # depending on TweepError.code, one may want to retry or wait
            # to keep things simple, we will give up on an error
            print (e)
        twit_count = 0
        for tweet in searched_tweets:
            #print (tweet)
            #print(tweet if (twit_count == 0) else "")
            
            max_id = tweet.id
            (print("initial id: ",max_id) if twit_count == 0 else "")
            author_info = {"name": tweet.author.name, "location": tweet.author.location}
            #date of creation / tweet id / author info / hastags / symbols / urls / retweet / text
            #csvWriter.writerow([tweet.created_at, tweet.id, author_info, tweet.entities["hashtags"], tweet.entities["symbols"], tweet.entities["urls"], tweet.retweet_count, tweet.full_text.encode('utf-8')])
            self.data_svc.register_tweet(
                            space = self.space,
                            tweet_id = str(tweet.id),
                            tweet_date = tweet.created_at, 
                            author_info = author_info, 
                            hashtag = tweet.entities["hashtags"], 
                            symbols = tweet.entities["symbols"], 
                            urls = tweet.entities["urls"], 
                            user_mensions = tweet.entities["user_mentions"], 
                            retweet = tweet.retweet_count, 
                            text = str(tweet.full_text.encode('utf-8')))
            twit_count += 1
        
        csvFile.close()
        #max_id = searched_tweets.page_iterator[]
        print ("final id: ",max_id)
        return max_id


#fetcher = Tweet_hastag_fetcher()
#fetcher.run()




# import service.data_service as data_svc


# # twitter setup
# consumer_key = "3cSaGgMXZGNtHw2nGMzS67oZ0"
# consumer_secret = "uK2Ny7rD0RYmjku54LVpRjxG6EPMGYKmzkHAze1XT1OgpDHDEf"
# access_token = "933397205985218570-stOqCQwrfaj66WdxKZxWaPtu7SVjPqJ"
# access_token_secret = "STPtNp6QhwGylbuFYd73UXQ7FT6GYSWYcr6GdUMHJnBQ8"
# # Auth
# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)
# api = tweepy.API(auth) 


# from datetime import datetime, timedelta

# def normalize_timestamp(time):
#     mytime = datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
#     mytime += timedelta(hours=1)   # the tweets are timestamped in GMT timezone, while I am in +1 timezone
#     return (mytime.strftime("%Y-%m-%d %H_%M_%S")) 


# def compute_get_twit_count(x):
#     x = x +1



# def get_twitter_data_search(last_id = -1):
#     query = "#Corrupcion"
#     max_tweets = 1000
#     searched_tweets = []
#     csvFile = open('ua.csv', 'a')
#     #Use csv Writer
#     csvWriter = csv.writer(csvFile)
#     while len(searched_tweets) < max_tweets:
#         count = max_tweets - len(searched_tweets)
#         print(str(last_id))
#         try:
#             new_tweets = api.search(q=query, count=count, since="2019-06-02", since_id=str(last_id), lang = "es")
#             print (len(new_tweets))
#             if not new_tweets:
#                 print ("not founded")
#                 break
#             searched_tweets.extend(new_tweets)
#             print("first id: ", new_tweets[len(new_tweets)].id)
#             last_id = new_tweets[0].id
#         except tweepy.TweepError as e:
#             # depending on TweepError.code, one may want to retry or wait
#             # to keep things simple, we will give up on an error
#             print (e)
#             print ("error")
#             break
#     twit_count = 0
#     for tweet in searched_tweets:
#         csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
#         twit_count += 1
# #         record = ''
# #         record += str(i.user.id_str)
# #         record += ';'
# #         record += str(normalize_timestamp(str(i.created_at)))
# #         record += ';'
# #         record += str(i.user.followers_count)
# #         record += ';'
# #         record += str(i.user.location)
# #         record += ';'
# #         record += str(i.favorite_count)
# #         record += ';'
# #         record += str(i.retweet_count)
# #         record += ';'
#         #producer.send(topic_name, str.encode(record))
#     return twit_count, last_id #searched_tweets#

# ###############################3 with cursor


# searched_tweets = []
# def get_twitter_data_cursor(last_id = -1, since_date = "2019-06-07", file_name = "tweet_aux"):
#     since_date = since_date
#     last_id = last_id
#     query = "guatemala"
#     max_tweets = 1000
#     max_id = 0
#     searched_tweets = []
#     print(str(datetime.now()))
#     csvFile = open(file_name+'.csv', 'a', newline = '')
#     #Use csv Writer
#     csvWriter = csv.writer(csvFile)
# #     while True:#len(searched_tweets) < max_tweets:
#         #count = max_tweets - len(searched_tweets)
#     print("last_id: ",str(last_id))
#     try:
#         new_tweets = tweepy.Cursor(api.search,
#                         tweet_mode='extended',
#                         q=query,
#                         count=max_tweets,
#                         lang = "es",
#                         since= since_date,
#                         max_id = str(last_id)).items()
#         # if not new_tweets:
#         #     print ("not founded")
#         searched_tweets = new_tweets
        
#         #print("finished", new_tweets)#searched_tweets)
#     except tweepy.TweepError as e:
#         # depending on TweepError.code, one may want to retry or wait
#         # to keep things simple, we will give up on an error
#         print (e)
#     twit_count = 0
#     for tweet in searched_tweets:
#         #print (tweet)
#         #print(tweet if (twit_count == 0) else "")
        
#         max_id = tweet.id
#         (print("initial id: ",max_id) if twit_count == 0 else "")
#         author_info = {"name": tweet.author.name, "location": tweet.author.location}
#         #date of creation / tweet id / author info / hastags / symbols / urls / retweet / text
#         #csvWriter.writerow([tweet.created_at, tweet.id, author_info, tweet.entities["hashtags"], tweet.entities["symbols"], tweet.entities["urls"], tweet.retweet_count, tweet.full_text.encode('utf-8')])
#         data_svc.register_tweet(str(tweet.id), tweet.created_at, author_info, tweet.entities["hashtags"], tweet.entities["symbols"], tweet.entities["urls"], tweet.entities["user_mentions"], tweet.retweet_count, str(tweet.full_text.encode('utf-8')))
#         twit_count += 1
    
#     csvFile.close()
#     #max_id = searched_tweets.page_iterator[]
#     print ("final id: ",max_id)
#     return max_id



# ### Deployment 

# def periodic_work(interval):
#     get_count = 0
#     twit_count = 0
#     count = 0
#     last_id = -1
#     while True:
#         count += 1
#         get_count += 1
#         aux_twit_count , last_id = get_twitter_data_search(last_id)
#         print (str(last_id)+" ; "+str(aux_twit_count))
#         twit_count += aux_twit_count
#         if count == 20:
#             print("twit_count: ",twit_count)
#             twit_count = 0
#         #interval should be an integer, the number of seconds to wait
#         time.sleep(interval)

# def periodic_work_cursor(interval = 30):
#     work_space = '.\\storage\\'
#     file_name = work_space+'tweet'+str(datetime.now().strftime("%Y-%m-%d %H_%M_%S"))
#     last_id = 0
#     fetch_count = 0
#     while True:
#         last_id = get_twitter_data_cursor(last_id = last_id, since_date= "2019-03-6", file_name= file_name)
#         time.sleep(interval)
#         fetch_count += 1
#         print("fetch count: ", fetch_count)

#  # get data every couple of minutes

# def main_tweet_search():
#     # searched_tweets = []
#     #get_twitter_data_search(-1)
#     periodic_work_cursor(30) 
#     # last_id = get_twitter_data_cursor(since_date= "2019-06-05")
#     # get_twitter_data_cursor(last_id= last_id, since_date= "2019-06-04")
# # main_tweet_search()