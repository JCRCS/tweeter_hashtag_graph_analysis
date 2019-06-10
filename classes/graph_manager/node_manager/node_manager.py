# import service.data_service as data_svc
# import classes.graph_manager.node_manager.node_maker_hastag as node_maker_hashtag

from service.data_service import *
from classes.graph_manager.node_manager.node_maker_hastag import *

class Node_manager():
    def __init__(self):
        self.data_svc = Data_service()
        space = self.data_svc.get_space("gt")
        self.node_maker_hashtag = Node_maker_hashtag(space)

    def run(self, node_type_name = ""):
        self.node_maker_hashtag.run()
        print("Node_manager")
    