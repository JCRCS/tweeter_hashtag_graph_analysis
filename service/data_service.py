import datetime
import bson
from typing import List
import pandas as pd
import re

 
from data.graph import Graph
from data.hashtag import Hashtag
from data.space import Space
from data.tweet import Tweet



def register_tweet(text: Entity, typeObjUri: str) -> TypeObj:
    """add a type to a entity
        args*:
            entity: Entity
                the Entity where will be stored the typeObj
            typeObjUri: str
                the typeObj URI to register into the Entity
        return:
            typeObj
                return the typeObj registered
    """
    typeObj = TypeObj()
    typeObj.entity_id = entity.id
    typeObj.typeObjUri = typeObjUri
    typeObj.save()
    
    #entity = Entity.objects(id = entity.id).first()
    entity.typeObj_ids.append(typeObj.id)
    entity.save()

    return typeObj