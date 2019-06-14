import datetime
import bson
from typing import List
import pandas as pd
import re
import numpy as np

 
from data.graph import Graph
from data.node import Node
from data.space import Space
from data.tweet import Tweet
from data.node_type import Node_type

class Data_service():
    def __init__(self):
        pass

    def register_graph(self, name:str) -> Graph:
        """add a graph of tweeters
            *args:
                name: str
            return 
                graph: Graph
                    return the graph created
        """

        #IF graph all ready exists: DO nothing
        graph = Graph.objects(name = name).first()
        if graph != None:
            print("graph allready exists")
            return graph
        else:
            pass
        graph = Graph()
        graph.name = name
        graph.save()
        return graph
    
    def register_edges(self, graph: Graph, edges: list)-> Graph:
        """ 
        this method register the edges in a graph
        where an edge is a tuple of node_id
            *args:
                graph: Graph
                    graph were the edges will be created
                edges: [(node_id,node_id)]
                    array that contains a tuple of the node_ids 
                    to relate
            return:
                graph:Graph
                    the graph with the edges created
        """
        stored_edges = []
        for iEdge in edges:
            stored_edge = self.register_edge(graph, iEdge)
            stored_edges.append(stored_edge) if stored_edge != None else None
        return stored_edges
    
    def register_edge(self, graph: Graph, edge: tuple) -> Graph:
        if edge not in graph.edges:
            #print (f"{edge} didn't exists")
            graph.edges.append(edge)
            graph.save()
            return edge
        else:
            pass#print(f"{edge} edge all ready exist")
        

    
    def register_node_type(self, name:str) -> Node_type:
        """add a node_type of nodes
            *args:
                name: str
            return 
                node_type: Node_type
                    return the node_type created
        """
        #IF node_type all ready exists: RETURN all ready exists note_type
        node_type = Node_type.objects(name = name).first()
        if node_type != None:
            #print("node_type all ready exists")
            return node_type
        else:
            pass
        node_type = Node_type()
        node_type.name = name
        node_type.save()
        return node_type
    
    def register_node(self, name: str, node_type: Node_type,  node_type_id = 0, root = "") -> Node:
        """ add a node with a node_type
            *args:
                node_type: Node_type
         """
        def register_root( node: Node, root = ""):
            if root is None:
                pass
                #print(f"node: {node.name}, doesn't have root")
            elif root in node.roots:
                pass
                #print(f"root {root} allready exists in node")
                # #PROVISIIIIOOONALLLLLL!!!!!
                # node.roots.append(root)
                # node.save()
            else:
                node.roots.append(root)
                node.save()
            return root
        #IF Node_type is not specify: DO nothing
        if node_type == None and node_type_id == 0:
            print("specify the node_type")
            return
        elif node_type_id == 0:
            pass
        elif node_type == None:
            node_type = Node_type.objects(id = node_type_id).first()
        
        node = Node.objects(name = name).first()
        if node != None:
            print(f"node {node.name}, all ready exists")
            root = register_root(node= node, root = root)
            return node
        else:
            pass
        
        node = Node()
        node.name = name
        node.node_type_id = node_type.id
        root = register_root(node = node, root = root)
        node.save()
            
        node_type.nodes.append(node.id)
        node_type.save()
        return node


    def register_space(self, name:str) -> Space:
        """add a space of tweeters
            *args:
                name: str
            return 
                space: Space
                    return the space created
        """
        #IF space all ready exists: DO nothing
        space = Space.objects(name = name).first()
        if space != None:
            print(f"space: {space.name}, all ready exists")
            return space
        else:
            pass
        space = Space()
        space.name = name
        space.save()
        return space

    def register_tweet(self, tweet_id, tweet_date, author_info, hashtag, symbols, 
                        user_mensions, urls, retweet, text:str, space = None, space_id = 0 ) -> Tweet:
        """add a tweeter to a space
            args*:
                tweet_id: str
                tweet_date: DateTime
                author_info: {}
                hashtag: []
                symbols: []
                user_mensions: []
                urls: []
                retweet: Int 
                text: str
            return:
                tweet
                    return the registered tweet
        """
        #IF space is not specify: DO nothing
        if space == None and space_id == 0:
            print("specify the space")
            return
        elif space_id == 0:
            pass
        elif space == None:
            space = Space.objects(id = space_id).first()

        #IF tweet exist: DO nothing
        tweet = Tweet.objects(tweet_id = tweet_id).first()
        if tweet != None:
            if tweet.space_id == space.id:
                print("all ready exists")
                return None
            else:
                pass
        else:
            pass
        
        tweet = Tweet()
        tweet.space_id = space.id
        tweet.tweet_id = tweet_id
        tweet.tweet_date = tweet_date
        tweet.author_info = author_info
        tweet.hashtag = hashtag
        tweet.symbols = symbols
        tweet.urls = urls
        tweet.retweet = retweet
        tweet.hastag = []
        tweet.user_mensions = user_mensions
        tweet.text = text
        tweet.save()    
            
        space.tweets.append(tweet.id)
        space.save()

        return tweet

    



    
    def register_hashtag_tweet(self, node_id: str, tweet: Tweet) -> Tweet:
        """ register the hashtag node created on the tweeter
            *args:
                node: Node
            return:
                tweet: Tweet
        
         """
        tweet.hashtag_nodes.append(node_id)
        tweet.save()
        return tweet
    
    def create_hashtag_node(self):
        import mongoengine
        tweet.hashtag_nodes = mongoengine.ListField()



    def get_tweets(self, space = None, space_id = 0) -> List[Tweet]:
        """ fetch all the tweets to the take the hashtag with 
            another metod
            *args:
                space: Space = (defualt) None
                space_id: Int = (default) 0
            return
                list(tweets): List(Tweet) 
            
        """
        #IF space is not specify: DO nothing
        if space == None and space_id == 0:
            print("specify the space")
            return
        elif space_id == 0:
            pass
        elif space == None:
            space = Space.objects(id = space_id).first()

        tweets = Tweet.objects(id__in = space.tweets).all()

        return list(tweets)

    def get_space(self, name: str) -> Space:
        """ 
        give the existant espace that has the specific space_name
            *args:
                name:str
            return:
                space: Space
        
         """
        space = Space.objects(name = name).first()
        return space
    
    def get_nodes_with_roots(self, node_type: Node_type, root1: Space, root2: Space):
        """ 
        this method will return the allowed nodes, due to the rule
        that the nodes have to be more than one root
            *args:
                node_type: Node_type
                root1: Space.id
                root2: Space.id
            return:
                list(node_id): list(int)
        """
        print("entry to roots")
        nodes = Node.objects().all() \
            .filter(node_type_id=node_type.id)\
            .filter(roots__1__exists =True)\
            .filter(roots = root2.id)\
            .filter(roots = root1.id)
        print("it works!!!!!!!!! to find the root")
        #.filter(roots__1__exists =True)\
        return list(nodes)

    def get_node(self, node_id: str) -> Node:
        node = Node.objects(id = node_id).first()
        return node

    def get_io_tweets(self, space: Space):
        """ 
        this method finds the minimum and max.
        id of the tweets in db
            *args:
                space: Space
            return:
                (mayor_id, minor_id): () 
        """
        tweets = Tweet.objects().all()
        tweets_ids = [iTweet.tweet_id for iTweet in tweets]
        tweets_sorted_ids = np.sort(tweets_ids)
        mayor_id = tweets_sorted_ids[-1] 
        minor_id = tweets_sorted_ids[0]
        print("mayor, minor")
        print(mayor_id, minor_id)
        return (mayor_id, minor_id)



