# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 12:00:44 2021

@author: prasaanth s
"""

def base_freq(dna):
    
    freq  = dict()
    
    for key in dna:
        
        if key not in freq:
            freq[key] = 1
        
        else:
            freq[key] += 1 
     
    return freq 
    
dna = str(input('Enter the input dna string  : ') )
dna.upper()

if dna.isalpha() :
    for x in dna:
        if x != 'A' or x != 'T' or x != 'C' or x != 'G':
          break
            
    print(base_freq(dna))
    
else :
    print('Invalid input ')    