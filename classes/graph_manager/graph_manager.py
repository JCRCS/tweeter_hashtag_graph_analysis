
# import classes.graph_manager.node_manager.node_manager as node_manager
# import service.data_service as data_svc

from classes.graph_manager.node_manager.node_manager import *
from service.data_service import *


class Graph_Manager():
    def __init__(self):
        self.node_manager = Node_manager()
        self.data_svc = Data_service()
        
    def run(self):
        print("Graph_manager")
        self.node_manager.run()
    
    def set_graph(self, name = ""):
        graph = self.data_svc.register_graph(name)
        return graph
    
    def create_edges(self, graph, nodes_to_relate = [] ):
        """ 
        create edges from teh relation that each tweeter contains,
        in terms of their hashtags
            *args:
                graph: Graph()
                    the graph to create_edges
                nodes_to_relate: []
                    the nodes to make the edges in the graph
            return:
                graph: Graph
         """
        edges = []
        if nodes_to_relate == []:
            print ("there is not edges to put")
            return graph
        for iNode_to_relate in nodes_to_relate:
             edges.extend([(iNode_to_relate, jNode_to_relate) for jNode_to_relate in nodes_to_relate if iNode_to_relate != jNode_to_relate ])
        if edges != []:
            graph = self.data_svc.register_edges( graph, edges)
        return graph

