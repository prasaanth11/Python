# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 00:09:06 2021

@author: prasaanth s
"""

def most_frequency(string):
    freq = dict()
    
    for key in string:
        if key not in freq:
            freq[key] = 1
        else:
            freq[key] += 1
            
    return sorted(freq.items(),key = lambda item : item[1], reverse=True)


def check_word(word):
    x =  word.isalpha()
    return x

word = input('Enter the input string  :  ')
s = check_word(word)

if s == True:
    print(most_frequency(word))
else:
    print("Not a  good input \n")
    