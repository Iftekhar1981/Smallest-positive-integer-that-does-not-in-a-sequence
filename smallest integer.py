# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 10:56:45 2021

@author: 47483
"""

def solution(A):
    Mx = max(A)
    if Mx < 1:
       return 1
   
    A.sort()
    Mn = min(A)
    
    
    for i in range(0, len(A)):    
        if Mn==A[i]:
            Mn=Mn+1
        else:
            smallest=Mn
            
    return smallest


# A = [1, 3, 6, 4, 1, 2]
A = [-11, -3, 0]

print(solution(A))