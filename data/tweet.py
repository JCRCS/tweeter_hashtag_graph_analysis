import datetime
import mongoengine


class Tweet(mongoengine.Document):
    """ this is the Tweet object that contains
     #date of creation / tweet id / author info / hastags / symbols / urls / retweet / text
        *args:
                space: space
                tweet_id: str
                tweet_date: DateTime
                author_info: {}
                hashtag: []
                symbols: []
                user_mensions: []
                urls: []
                retweet: Int 
                text: str
                text: {columnId : column}
                hashtag_nodes: List[Node_id]
    """
    space_id = mongoengine.ObjectIdField()
    tweet_id = mongoengine.StringField(required=True)

    registered_date = mongoengine.DateTimeField(default=datetime.datetime.now)
    tweet_date = mongoengine.DateTimeField()
    author_info = mongoengine.DictField()
    hashtag = mongoengine.ListField()
    symbols = mongoengine.ListField()
    user_mensions = mongoengine.ListField()
    urls = mongoengine.ListField()
    retweet = mongoengine.IntField()
    text = mongoengine.StringField()

    hashtag_nodes = mongoengine.ListField()
    

    meta = {
        'db_alias': 'core',
        'collection': 'tweet'
    }