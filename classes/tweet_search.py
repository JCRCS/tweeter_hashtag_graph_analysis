import tweepy
import time
import csv
import datetime


# twitter setup
consumer_key = "3cSaGgMXZGNtHw2nGMzS67oZ0"
consumer_secret = "uK2Ny7rD0RYmjku54LVpRjxG6EPMGYKmzkHAze1XT1OgpDHDEf"
access_token = "933397205985218570-stOqCQwrfaj66WdxKZxWaPtu7SVjPqJ"
access_token_secret = "STPtNp6QhwGylbuFYd73UXQ7FT6GYSWYcr6GdUMHJnBQ8"
# Auth
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth) 


from datetime import datetime, timedelta

def normalize_timestamp(time):
    mytime = datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
    mytime += timedelta(hours=1)   # the tweets are timestamped in GMT timezone, while I am in +1 timezone
    return (mytime.strftime("%Y-%m-%d %H_%M_%S")) 


def compute_get_twit_count(x):
    x = x +1



def get_twitter_data_search(last_id = -1):
    query = "#Corrupcion"
    max_tweets = 1000
    searched_tweets = []
    csvFile = open('ua.csv', 'a')
    #Use csv Writer
    csvWriter = csv.writer(csvFile)
    while len(searched_tweets) < max_tweets:
        count = max_tweets - len(searched_tweets)
        print(str(last_id))
        try:
            new_tweets = api.search(q=query, count=count, since="2019-06-02", since_id=str(last_id), lang = "es")
            print (len(new_tweets))
            if not new_tweets:
                print ("not founded")
                break
            searched_tweets.extend(new_tweets)
            print("first id: ", new_tweets[len(new_tweets)].id)
            last_id = new_tweets[0].id
        except tweepy.TweepError as e:
            # depending on TweepError.code, one may want to retry or wait
            # to keep things simple, we will give up on an error
            print (e)
            break
    twit_count = 0
    for tweet in searched_tweets:
        csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
        twit_count += 1
#         record = ''
#         record += str(i.user.id_str)
#         record += ';'
#         record += str(normalize_timestamp(str(i.created_at)))
#         record += ';'
#         record += str(i.user.followers_count)
#         record += ';'
#         record += str(i.user.location)
#         record += ';'
#         record += str(i.favorite_count)
#         record += ';'
#         record += str(i.retweet_count)
#         record += ';'
        #producer.send(topic_name, str.encode(record))
    return twit_count, last_id #searched_tweets#

###############################3 with cursor


searched_tweets = []
def get_twitter_data_cursor(last_id = -1, since_date = "2019-06-07", file_name = "tweet_aux"):
    since_date = since_date
    last_id = last_id
    query = "#guatemala"
    max_tweets = 1000
    max_id = 0
    searched_tweets = []
    print(str(datetime.now()))
    csvFile = open(file_name+'.csv', 'a', newline = '')
    #Use csv Writer
    csvWriter = csv.writer(csvFile)
#     while True:#len(searched_tweets) < max_tweets:
        #count = max_tweets - len(searched_tweets)
    print("last_id: ",str(last_id))
    try:
        new_tweets = tweepy.Cursor(api.search,
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
        csvWriter.writerow([tweet.created_at, max_id, tweet.full_text.encode('utf-8')])
        twit_count += 1
    
    csvFile.close()
    #max_id = searched_tweets.page_iterator[]
    print ("final id: ",max_id)
    return max_id



### Deployment 

def periodic_work(interval):
    get_count = 0
    twit_count = 0
    count = 0
    last_id = -1
    while True:
        count += 1
        get_count += 1
        aux_twit_count , last_id = get_twitter_data_search(last_id)
        print (str(last_id)+" ; "+str(aux_twit_count))
        twit_count += aux_twit_count
        if count == 20:
            print("twit_count: ",twit_count)
            twit_count = 0
        #interval should be an integer, the number of seconds to wait
        time.sleep(interval)

def periodic_work_cursor(interval = 30):
    work_space = '.\\storage\\'
    file_name = 'tweet'+str(datetime.now().strftime("%Y-%m-%d %H_%M_%S"))
    last_id = 0
    fetch_count = 0
    while True:
        print("fetch count: ", fetch_count)
        fetch_count += 1
        last_id = get_twitter_data_cursor(last_id = last_id, since_date= "2019-03-5")
        time.sleep(interval)


 # get data every couple of minutes

def main():
    # searched_tweets = []
    #get_twitter_data_search(-1)
    periodic_work_cursor(30) 
    # last_id = get_twitter_data_cursor(since_date= "2019-06-05")
    # get_twitter_data_cursor(last_id= last_id, since_date= "2019-06-04")
main()