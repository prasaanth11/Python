# -*- coding: utf-8 -*-
"""
@author: prasaanth s
"""

import numpy as np

def is_symmetric(matrix , r , c):
    
    for i in range(c):
        for j in range(r):
            if matrix[i][j] != matrix[j][i]:
                return False

    return True            


def is_stochastic (matrix , r, c):
    
    matrix = np.array(matrix)
    
    for x in matrix:
        if float(sum(x)) == 1.0:
            if all(0 <= y <= 1.0 for y in x) is False:
                return False
            else:
                return True
            

def is_orthogonal(matrix , r , c ):
    if r != c:
        return False
    
    for i in range(c):
        for j in range(c):
         
            sum = 0            
            for k in range (c):
                sum = sum + int(matrix[i][k] * matrix[j][k])
            
        
        if i == j and sum != 1:
            return False
         
        if i!=j and sum!=0:
            return False
    
    return True


r = int(input('Enter the number of rows   :  '))
c = int(input('Enter the number of columns :  '))

matrix = []

for i in range(r):
    a = []
    
    for j in range(c):
        a.append(int(input()))
        
    matrix.append(a)
    
print('\n\n')

if is_symmetric(matrix , r ,c ) :
    print('\nthe entered matrix is symmetric matrix \n')
else :
    print('\nthe entered matrix is not symmetric  matrix  \n')    

if is_stochastic (matrix , r ,c ) :
    print('\nthe entered matrix is stochastic matrix  \n')
else :
    print('\nthe entered matrix is not a stochastic matrix  \n')    

if is_orthogonal(matrix , r , c) :
    print('the entered matrix is a orthogonal matrix  \n')    
else:
    print('the entered matrix is not  a  orthogonal  matrix \n')    