#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 18:27:43 2019
@author: kampamocha
Jaccard similarity over sets
"""

def similarity(source, target, cost=1):
    """Jaccard similarity"""   
    if len(source) == 0 and len(target) == 0:
        return 1
    s = set(source)
    t = set(target)
    return len(set.intersection(s, t)) / len(set.union(s, t))

def distance(source, target, cost=1):
    """Jaccard distance"""
    return 1 - similarity(source, target, cost=1)
   
if(__name__ == '__main__'):
    print("Jaccard similarity")
