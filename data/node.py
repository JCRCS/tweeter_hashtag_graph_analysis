import datetime
import mongoengine

class Node(mongoengine.Document):
    """ this is the Hashtag object that contains
        *args:
                node_type_id: id
                name: str
    """
    node_type_id = mongoengine.ObjectIdField()
    
    registered_date = mongoengine.DateTimeField(default=datetime.datetime.now)
    name = mongoengine.StringField(required=True)
    roots = mongoengine.ListField()
    

    meta = {
        'db_alias': 'core',
        'collection': 'node'
    }