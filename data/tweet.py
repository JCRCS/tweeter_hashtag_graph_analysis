import datetime
import mongoengine


class Tweet(mongoengine.Document):
    """ this is the Tweet object that contains
     #date of creation / tweet id / author info / hastags / symbols / urls / retweet / text
        *args:
                 tweet_id: str
                tweet_date: DateTime
                author_info: {}
                hashtag: []
                symbols: []
                user_mensions: []
                urls: []
                retweet: Int 
                text: str
                id_tweet: str
                text: {columnId : column}
    """
    
    registered_date = mongoengine.DateTimeField(default=datetime.datetime.now)
    tweet_id = mongoengine.StringField(required=True)
    tweet_date = mongoengine.DateTimeField()
    author_info = mongoengine.DictField()
    hashtag = mongoengine.ListField()
    symbols = mongoengine.ListField()
    user_mensions = mongoengine.ListField()
    urls = mongoengine.ListField()
    retweet = mongoengine.IntField()
    hastags = mongoengine.ListField()
    text = mongoengine.StringField()
    

    meta = {
        'db_alias': 'core',
        'collection': 'tweet'
    }