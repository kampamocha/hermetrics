#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 18:27:43 2019
Jaro Winkler similarity
@author: kampamocha
"""
# https://en.wikipedia.org/wiki/Jaro%E2%80%93Winkler_distance
# http://richardminerich.com/tag/jaro-winkler/

from .jaro import Jaro

class JaroWinkler(Jaro):

    def __init__(self, name='Jaro-Winkler'):
        super().__init__(name=name)

    def similarity(self, source, target, cost=1, p=0.1):
        """Jaro Winkler similarity"""
        assert(0 <= p <= 0.25), "The p parameter must be between 0 and 1/4 inclusive"
        
        max_l = 4    
        l = 0
        
        for s, t in zip(source[:max_l], target[:max_l]):
            if s != t:
                break
            l += 1
        
        j = super().similarity(source, target, cost)
        w = j + l*p*(1-j)   
        
        return w
    
    def distance(self, source, target, cost=1, p=0.1):
        """Jaro Winkler distance"""
        return 1 - self.similarity(source, target, cost, p)
    
if(__name__ == '__main__'):
    print("Jaro Winkler similarity")
