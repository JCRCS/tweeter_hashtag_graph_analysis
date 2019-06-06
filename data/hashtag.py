import datetime
import mongoengine

class Hashtag(mongoengine.Document):
    """ this is the Hashtag object that contains
        *args:
                name: str
    """
    registered_date = mongoengine.DateTimeField(default=datetime.datetime.now)
    name = mongoengine.StringField(required=True)

    meta = {
        'db_alias': 'core',
        'collection': 'hashtag'
    }