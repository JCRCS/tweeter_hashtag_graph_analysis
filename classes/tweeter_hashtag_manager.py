from classes.space_manager import *
from classes.graph_manager.graph_manager import *
import networkx as nx
import matplotlib.pyplot as plt


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
        #self.create_graph_tweeter(space_name = "gt")

    def fetch_tweeter_interaction(self, queries, space_names, node_type_name):
        #CREATE/TAKE spaces, from the spaces names
        spaces = [self.space_manager.set_space(name = iSpace_name) for iSpace_name in space_names]
        #LOOP in queries and in spaces
        for iQuery, iSpace in zip(queries, spaces):
            #FETCH tweets, from each query and space
            self.space_manager.fetch_tweets(space = iSpace, query = iQuery)
    
    def create_hashtag_interaction(self, space_names, node_type_name):
        #CREATE/TAKE spaces, from the spaces names
        spaces = [self.space_manager.set_space(name = iSpace_name) for iSpace_name in space_names]
        #CREATE/TAKE the node_type, from the node_manager of the graph_manager
        node_type = self.graph_manager.node_manager.set_node_type(node_type_name = node_type_name)
        #CREATE/TAKE the hashtag nodes, from the tweeter
        for iSpace in spaces:
            self.create_hashtag_nodes(space = iSpace, node_type = node_type)
    
    def graph_hashtag_interaction(self, space_names, graph_name, node_type_name):
        """
        this is a method that collects the tweeters from the queries and creates a
        tweeter space for each, make the node_type and connects it into a graph
            *args:
                queries: []
                space_names: []
                graph_name: str
                node_type_name: str
            return:
                graph??????
        """
        #CREATE/TAKE spaces, from the spaces names
        spaces = [self.space_manager.set_space(name = iSpace_name) for iSpace_name in space_names]
        #CREATE/TAKE the node_type, from the node_manager of the graph_manager
        node_type = self.graph_manager.node_manager.set_node_type(node_type_name = node_type_name)
        #CREATE/UPDATE a graph of hashtags connected by the appereances on the tweeters
        graph = self.graph_manager.set_graph(name= graph_name)
        self.create_graph_tweeter(node_type = node_type, graph = graph, spaces = spaces)


    def create_graph_tweeter(self, node_type: Node_type, graph: Graph, spaces = []):
        tweets = []
        for iSpace in spaces:
            tweets.extend(self.space_manager.get_tweets(iSpace))
        print(f"root1 {spaces[0]}, root2 {spaces[1]}")
        allowed_nodes = self.graph_manager.node_manager.get_nodes_with_roots(node_type = node_type, root1 = spaces[0], root2 = spaces[0])
        allowed_nodes_id = [iAllowed_node.id for iAllowed_node in allowed_nodes]
        g = self.graph_manager.set_plot_nodes(nodes = allowed_nodes_id)
        for iTweet in tweets:
            #print("checking the nodes of a new tweeter")
            nodes_in_tweet = self.space_manager.get_hashtags_nodes(tweet=  iTweet)
            #get the nodes to be part of the graph
            #depending on their roots
            #allowed_nodes
            #FIIIIIIIX THE CREATION OF THE EDGES BEFORE BEING REGISTERED THE ARE REPEATED!!!!
            nodes_to_relate = [iNode_to_relate for iNode_to_relate in nodes_in_tweet if iNode_to_relate in allowed_nodes_id]
            if nodes_to_relate != []:
                stored_edges = self.graph_manager.create_edges(graph, nodes_to_relate)
                self.graph_manager.set_plot_edges(g = g, edges = stored_edges)
        self.graph_manager.descrive_graph(g = g)


    def create_hashtag_nodes(self, space: Space, node_type: Node_type):
        """ create notes from the hashtags of the tweeters,
            also put into the tweeters the ids of the hashtag nodes 
            from one single space
            *args:
                space: Space
                node_type: Node_type
            return
                hashtags: List(Node)?????????
        """
        tweets = self.space_manager.get_tweets(space = space)
        for iTweet in tweets:
            self.create_hashtag_node(tweet = iTweet, node_type =node_type)


    def create_hashtag_node(self, tweet: Tweet, node_type: Node_type):
        """ create nodes from the hashtags of the tweeters,
            also put into the tweeters the ids of the hashtag nodes 
            *args:
                tweeters: List(Tweet
                node_type: Node_type
            return
                hashtags: List(Node)?????????
        """
        #TAKE the hashtags from the tweet
        try:
            hashtags = tweet.hashtag
        except:
            print(f"there isn't hashtags in tweet")
        #LOOP over the hashtags
        for iHashtag in hashtags:
            #CREATE/TAKE the node and assign it's roots
            node = self.graph_manager.node_manager.create_node(name = iHashtag["text"], node_type = node_type, root = tweet.space_id)
            #ASSIGN the created hashtag_node, to the tweet where it belongs
            self.space_manager.assign_tweet_hashtag(hashtag_id = node.id, tweet = tweet)
        
        
        #TAKE the user_mensions from the tweet
        try:
            user_mensions = tweet.user_mensions
        except:
            print(f"there isn't user_mensions in tweet")
        #LOOP over the user_mensions
        for iUser_mension in user_mensions:
            #CREATE/TAKE the node and assign it's roots
            node = self.graph_manager.node_manager.create_node(name = iUser_mension["screen_name"], node_type = node_type, root = tweet.space_id)
            #ASSIGN the created hashtag_node, to the tweet where it belongs
            self.space_manager.assign_tweet_hashtag(hashtag_id = node.id, tweet = tweet)
        
        #TAKE the urls from the tweet
        try:
            urls = tweet.urls
        except:
            print(f"there isn't urls in tweet")
        #LOOP over the urls
        for iUrl in urls:
            #CREATE/TAKE the node and assign it's roots
            node = self.graph_manager.node_manager.create_node(name = iUrl["url"], node_type = node_type, root = tweet.space_id)
            #ASSIGN the created hashtag_node, to the tweet where it belongs
            self.space_manager.assign_tweet_hashtag(hashtag_id = node.id, tweet = tweet)

    

