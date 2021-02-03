# -*- coding: utf-8 -*-
"""
@author: prasaanth s
"""
import math

n = int(input('Enter the number of tuples to be entered  :   '))

u = ()
v = ()

u = list(u) ; v = list(v)
print('\nEnter the value of u  :  ')

for i in range(n):
    ele = int(input())
    u.append(ele)
    

print('\nEnter the value of v  :  ')

for i in range(n):
    ele = int(input())
    v.append(ele)    
    
u = tuple(u) ; v = tuple(v)

distance = math.sqrt( sum([ (u-v)**2 for u,v in zip(u,v) ]) )

print('\n\nEuclidean distance  : ' + format(distance))