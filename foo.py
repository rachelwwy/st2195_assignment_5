#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 17:27:13 2024

@author: wongrachel
"""
'''
    Checks whether x is divisible by k.
'''

def is_divisible_by_k(x, k):   
    if (x%k == 0):
        print ("divisible")
        return (x)
   
    for x in range(1000):
       if is_divisible_by_k(x, 2) or is_divisible_by_k(x, 5) or is_divisible_by_k(x, 7):
         return(x)
     
    print(x)
    total = sum(x)
    print(total)
        
                 
       
'''
Store all the integers that are multiples of 2 or 5 or 7 that are lower or equal to 1000 (excluding doubles)
'''

for x in range(1000):
        if x%2 == 0 or x%5 ==0 or x%7 == 0:
            print(x)
            
            '''
Sum all the integers that are multiples of 2 or 5 or 7 that are lower or equal to 1000 (excluding doubles)
'''

        total_sum = sum(x for i in range(1000))
        print(total_sum)