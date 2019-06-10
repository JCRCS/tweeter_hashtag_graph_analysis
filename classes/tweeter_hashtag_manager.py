from classes.space_manager import *
from classes.graph_manager.graph_manager import *


class Tweeter_hashtag_manager():
    def __init__(self):
        self.space_manager = Space_Manager()
        self.graph_manager = Graph_Manager()
    
    def run(self):
        """ run the spaces of tweeter and the graph of hashtags
            *args:
            return:
            function:
        """
        print("runing tweeter_hashtag_manager")
        #self.space_manager.run()
        #self.graph_manager.run()
        self.create_graph_tweeter(space_name = "gt")
    
    def create_graph_tweeter(self, space_name: str):
        space = self.space_manager.set_space(name= space_name)
        graph = self.graph_manager.set_graph(name= "hashtag")
        tweets = self.space_manager.get_tweets(space)
        for iTweet in tweets:
            nodes_to_relate = self.space_manager.get_hashtags_relations(iTweet)
            if nodes_to_relate != []:
                self.graph_manager.create_edges(graph, nodes_to_relate)
