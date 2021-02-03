# -*- coding: utf-8 -*-
"""
@author: prasaanth s
"""
import math
import numpy as np

from scipy import spatial

n = int(input('Enter the value of n  :  '))

u = () 
v = ()

u = list(u) ; v = list(v)

print('\nEnter the values for u  :  ')

for i in range(n):
    ele = int(input())
    u.append(ele)
    
    
print('\nEnter the values for v  :  ')    

for i in range(n):
    ele = int(input())
    v.append(ele)  
    
    
u = tuple(u) ; v = tuple(v) 

distance = math.sqrt( sum([ (u-v)**2 for u,v in zip(u,v) ]) )

print('\n\nEuclidean distance  : ' + format(distance))    

print( 'similarity ' + format(1 - spatial.distance.cosine(u,v) ))
    
