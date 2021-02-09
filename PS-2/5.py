# -*- coding: utf-8 -*-
"""
@author: prasaanth s
"""

def normalization(x):
    n = list()

    for i in range(x):
        a = float(input())
        n.append(a)
    
    s = sum(n)

    norm = [i/s for i in n]
    
    return norm


x = int(input("Enter the number of elements to be inserted into the list  : "))
print('The normalized value for the entered set  : ' + normalization(x))
