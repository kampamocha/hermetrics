#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 12:19:17 2019
Dice Similarity a.k.a. Sorenson-Dice
@author: kampamocha
"""
import hermetrics.metrics.jaccard as jaccard

def similarity(source, target, cost=1):
    """Dice similarity"""   
    if len(source) == 0 and len(target) == 0:
        return 1
    
    J = jaccard.similarity(source)
    return 2 * J / (1 + J)

def distance(source, target, cost=1):
    """Dice distance"""
    return 1 - similarity(source, target, cost=1)
   
if(__name__ == '__main__'):
    print("Dice similarity")

