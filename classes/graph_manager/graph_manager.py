
# import classes.graph_manager.node_manager.node_manager as node_manager
# import service.data_service as data_svc

from classes.graph_manager.node_manager.node_manager import *
from service.data_service import *
import networkx as nx
import matplotlib.pyplot as plt


class Graph_Manager():
    def __init__(self):
        self.node_manager = Node_manager()
        self.data_svc = Data_service()
        self.g = None
        
    def run(self,space: Space):
        print("Graph_manager")
        self.node_manager.run(space)
    
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
            stored_edges = self.data_svc.register_edges( graph, edges)
            return stored_edges
    
    def set_plot_nodes(self, nodes = []):
        g = nx.Graph()
        #self.data_svc.get_node(node_id = node)
        [g.add_node(self.data_svc.get_node(iNode_id).name) for iNode_id in nodes]
        nx.info(g)
        nx.draw(g)
        plt.show()
        return g

    # def get_node(node_id: str):
    #     node = Node.objects(id = node_id).first()
    #     return node
    
    def set_plot_edges(self, g: nx.Graph, edges = []):
        #[g.add_edge(iEdge[0],iEdge[1]) for iEdge in edges]
        if edges !=None:
            edges = [(self.data_svc.get_node(iEdge[0]).name, self.data_svc.get_node(iEdge[1]).name) for iEdge in edges]
        g.add_edges_from(edges) if edges != None else None
        #print(nx.info(g))
        #nx.draw(g)
        #plt.show()
    
    def descrive_graph(self, g: nx.Graph, space_names):
        print("centrality")
        print(nx.degree_centrality(g))
        print("betwenness centrality")
        print(nx.betweenness_centrality(g))
        work_space = '.\\storage\\'
        nx.write_graphml(g, work_space +f"{space_names[0]}-{space_names[1]}.graphml")
        nx.draw(g)
        self.g = g
        plt.show()
    
    def import_graph(self, space_names):
        work_space = '.\\storage\\'
        g = nx.read_graphml(work_space+f"{space_names[0]}-{space_names[1]}.graphml")
        self.g = g
        return g 
