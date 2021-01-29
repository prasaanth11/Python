# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 00:46:45 2021

@author: prasaanth s
"""

alice_ratings = {"alonzo": 1, "bob": 3, "turing": 2}
bob_ratings = {"alice": 1, "alonzo": 2, "turing": 3}
alonzo_ratings = {"alice": 3, "bob": 2, "turing": 1}
turing_ratings = {"alice": 2, "alonzo": 1, "bob": 3}
friends = {"alice": alice_ratings, "bob": bob_ratings,"alonzo": alonzo_ratings, "turing": turing_ratings}


def most_popular():
    
    new_dict = dict.fromkeys(friends.keys(),0)
    
    for key,value in friends.items():
        for name, rate in value.items():
            new_dict[name] += rate
        
    temp = min(new_dict.values())   

    least = [key for key,value in new_dict.items() if value == temp]
    print(str(least))
    
    
most_popular()