# import service.data_service as data_svc
# import classes.graph_manager.node_manager.node_maker_hastag as node_maker_hashtag

from service.data_service import *
from classes.graph_manager.node_manager.node_maker_hastag import *

class Node_manager():
    def __init__(self):
        self.data_svc = Data_service()
        #self.node_maker_hashtag = Node_maker_hashtag()

    def run(self, space:Space, node_type_name = ""):
        print("Node_manager.Run execute")
        #self.node_maker_hashtag.run(space = space)
    
    def set_node_type(self, node_type_name: str):
        """ 
        this method allow to Node_manager to create a new data_type
        or to return an existing one  
            *args:
                node_type_name: str
            return:
                node_type: Node_type
        """
        node_type = self.data_svc.register_node_type(name = node_type_name)
        return node_type

    def create_node(self, name: str, node_type: Node_type, root: str):
        """ 
        this method allow to Node_manager to 
        creates a node in the 
            *args:
                name: str,
                node_type: Node_type
                root: str
            return:
                node: Node
                    returns the node that has been created 
                    in the db and seted the root where it 
                    comes
        """
        node = self.data_svc.register_node(root = root, name = name, node_type = node_type)
        return node
    
    def get_nodes_with_roots(self, node_type: Node_type, root1: Space, root2: Space):
        """ 
        this method will return the allowed nodes, due to the rule
        that the nodes have to be more than one root
            *args:
                node_type: Node_type
                numb_roots: int
            return:
                list(node_id): list(int)
        """
        nodes_id = self.data_svc.get_nodes_with_roots(node_type = node_type, root1 = root1, root2 = root2)
        return list(nodes_id) #ids

        
    