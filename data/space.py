import datetime
import mongoengine

class Space(mongoengine.Document):
    """ this is the Space object that contains
        *args:
                name: str
                tweets: [tweet_id]
    """
    registered_date = mongoengine.DateTimeField(default=datetime.datetime.now)
    name = mongoengine.StringField(required=True)
    tweets = mongoengine.ListField()

    meta = {
        'db_alias': 'core',
        'collection': 'space'
    }