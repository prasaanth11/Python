# -*- coding: utf-8 -*-
"""
@author: prasaanth s
"""

import numpy as np

r = int(input('Enter the number of rows :  '))
c = int(input('Enter the number of colums :  '))

matrix = []

print('\n\n Enter the matrix in rowwise : ')

for i in range(r):
    
    a = []
    for j in range(c):
        a.append(int(input()))
    
    matrix.append(a)
    
print('\n\n')

array_matrix = np.array(matrix)

print(np.linalg.inv(array_matrix))

