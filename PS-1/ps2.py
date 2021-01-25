# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 10:52:01 2021

@author: prasaanth s
"""

def recurrsion(S,n):
    
    if n==1 :
        return S[n-1]
    
    else:
        previous = recurrsion(S, n-1)
        current = S[n-1]
        
        if(current > previous) :
            return current
        
        else :
            return previous

listing = [1,2,3,4,5,6,7,8,9]
x = recurrsion(listing,9)

print(x)

