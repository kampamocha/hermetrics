#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 18:27:43 2019
Hamming distance 
@author: kampamocha
"""

# https://en.wikipedia.org/wiki/Hamming_distance
# In this version is not mandatory to have sme length strings
def distance(source, target, cost=1):
    """Hamming distance with right padding"""
    # Difference in length
    length_difference = abs(len(source) - len(target))
    dist = sum(s != t for s, t in zip(source, target))
    return  (length_difference + dist) * cost
    
def max_distance(source, target, cost=1):
    """Hamming maximum distance value"""
    return max(len(source), len(target)) * cost
    
if(__name__ == '__main__'):
    print("Hamming distance")
