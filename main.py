from colorama import Fore

#from classes.tweet_search import *
import data.mongo_setup as mongo_setup
# import classes.tweeter_hashtag_manager as tweeter_hashtag_manager
from classes.tweeter_hashtag_manager import *


def main():
    mongo_setup.global_init()
    my_tweeter_hashtag_manager = Tweeter_hashtag_manager()

    while True:
        print_header()

        choice = find_user_intent()
        space1 = "guatemala"#input("insert the first query ")
        space2 = "corrupcion"#input("insert the second query ")

        #space_names = [space1, space2]
        space_names = [space1, space2]
        node_type_name = "hashtag"
        graph_name = "hashtag"
        
        if choice == 'tweet':
            queries = [space1, space2]
            my_tweeter_hashtag_manager.fetch_tweeter_interaction(queries = queries, 
                space_names = space_names, 
                node_type_name = node_type_name)
        
        elif choice == 'nodes':
            my_tweeter_hashtag_manager.create_hashtag_interaction( 
                space_names = space_names, 
                node_type_name = node_type_name)

        elif choice == 'graph':
            my_tweeter_hashtag_manager.graph_hashtag_interaction(
                space_names = space_names, 
                graph_name = graph_name, 
                node_type_name = node_type_name)
        elif choice == 'describe':
            my_tweeter_hashtag_manager.graph_manager.descrive_graph(
                my_tweeter_hashtag_manager.graph_manager.g,
                space_names = space_names
            )
        elif choice == 'import':
            g = my_tweeter_hashtag_manager.graph_manager.import_graph(
                space_names = space_names
            )
            my_tweeter_hashtag_manager.graph_manager.descrive_graph(g, space_names = space_names)

        else:
            print("chose an option t,n,g ")
            return 'book'
    



# def main():
#     mongo_setup.global_init()

#     print_header()

#     try:
#         while True:
#             if find_user_intent() == 'book':
#                 program_guests.run()
#             else:
#                 program_hosts.run()
#     except KeyboardInterrupt:
#         return


def print_header():
    snake = \
""" 
___________$$$$$§§§§$$§§§$$$$$$
______$§§§$$_$§§$___§$__$§§§$$$§§§$$
____§§§§____$§______$______$§____§§§§$
__$§$$$____§§_______§_______$§$____§_§§
__§$_$____§§________§_________§____$§_§§
_§§_§_____§_________§_________$§____§$_§$
$§_$$____§§_________§__________§_____§_$§
§$_$_____§$_________§__________§$____§__§$
§__§_____§__________§__________$$____§$_§§
§__§_____§__________§__________$$____§$_$§
§__§_____§____DIGITAL BALOON___$$____§$_§§
§$_$$____$__________§__________$_____§__§$
$§__§____$$___$$____§_____$§___§____$§_$§
_§§_$_$§$_$_$§§§§$__$__$§§§§§__$_$§§§_$§
__§§§§§§§§§§§§_$§§§$§§§§§$$§§§§§§§§§§§§$
___§§§J$_$§§§_____§§§§§_____$§§§$__§§§$
____$h§____§________§$_______$$___$$§$
_____$§$____$_______$________$___$§§$
______$§$___§_______§_______$$___§§
_______$§$___§______§_______§___§§
_________§$__§$_____§______§___§§
__________§§__§_____§_____$$__§§
___________§§__§____$_____§_$§$
____________§§_$§__$§___$§_$§$
_____________$§§§§§§§§§§§§§§
_______________$____$§____$
_______________$____$§___$$
______________$§$$$$§$$$$$$$
______________$§$__$§$___$§§
_______________$$__$$____$$$
_______________$$$$_§$_$$$§

welcome to the social digital baloon where you can see 
from a new perspective the social digital world.
 """

    print(Fore.WHITE + '*******  welcome to the social DIGITAL BALOON where you can see  ********')
    print(Fore.WHITE + '*******     from a new perspective the social digital world.     ********')
    print(Fore.GREEN + snake)
    print(Fore.WHITE + '*************************************************************************')
    print()
    print("Welcome to Digital Baloon")
    print("What do you want to do?:")
    print()


def find_user_intent():
    print("     [t] fetch tweets")
    print("     [n] create nodes from tweets")
    print("     [g] create graph from nodes")
    print("     [d] describe graph of the spaces")
    print("     [i] import graph from the spaces")
    print()
    choice = input("Choose an option: ")
    if choice == 't':
        return 'tweet'
    elif choice == 'n':
        return 'nodes'
    elif choice == 'g':
        return 'graph'
    elif choice == 'd':
        return 'describe'
    elif choice == 'i':
        return 'import'


main()

