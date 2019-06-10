import datetime
import mongoengine

class Node_type(mongoengine.Document):
    """ this is the Space object that contains tweeters id
        *args:
                name: str
                tweets: [tweet_id]
    """
    registered_date = mongoengine.DateTimeField(default=datetime.datetime.now)
    name = mongoengine.StringField(required=True)
    nodes = mongoengine.ListField()

    meta = {
        'db_alias': 'core',
        'collection': 'node_type'
    }