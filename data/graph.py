import datetime
import mongoengine

class Graph(mongoengine.Document):
    """ this is the graph object that contains
        *args:
                name: str
    """
    registered_date = mongoengine.DateTimeField(default=datetime.datetime.now)
    name = mongoengine.StringField(required=True)
    edges = mongoengine.ListField()

    meta = {
        'db_alias': 'core',
        'collection': 'graph'
    }