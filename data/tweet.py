import datetime
import mongoengine

class Tweet(mongoengine.Document):
    """ this is the Tweet object that contains
        *args:
                id_tweet: str
                text: {columnId : column}
    """
    registered_date = mongoengine.DateTimeField(default=datetime.datetime.now)
    id_tweet = mongoengine.StringField(required=True)
    hastags = mongoengine.ListField()

    meta = {
        'db_alias': 'core',
        'collection': 'tweet'
    }