#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 15:27:52 2019
Python library for distance and similarity metrics
@author: kampamocha
"""

class Metric:
    """Class for metric implementations"""

    def __init__(self, distance=None, max_distance=None, min_distance=None, normalize=None, normalized_distance=None,  similarity=None, name='Generic'):
        """Class constructor - receives a function for distance or similarity evaluation"""
        self.name = name
        self.distance = distance or self.distance
        self.max_distance = max_distance or self.max_distance
        self.min_distance = min_distance or self.min_distance
        self.normalize = normalize or self.normalize        
        self.normalized_distance = normalized_distance or self.normalized_distance
        self.similarity = similarity or self.similarity

    def __repr__(self):
        """Class representation"""
        return f'Metric({self.name!r})'

    # Default methods
    def distance(self, source, target, cost=1):
        """Default distance function, 0 for equal, 1 for not equal"""
        return 0 if source == target else 1
    
    def max_distance(self, source, target, cost=1):
        """Maximum distance value"""
        if len(source) == 0 and len(target) == 0:
            return 0
        return 1
    
    def min_distance(self, source, target, cost=1):
        """Minimum distance value"""
        return 0

    def normalize(self, x, high=1, low=0):
        """Function for value normalization"""
        if x >= high:
            return 1
        if x <= low:
            return 0
        return (x - low) / (high - low)
       
    def normalized_distance(self, source, target, cost=1):
        """Normalized distance between two objects"""
        return self.normalize(self.distance(source, target, cost), self.max_distance(source, target, cost), self.min_distance(source, target, cost))
    
    def similarity(self, source, target, cost=1):
        """Normalized similarity between two objects"""
        return 1 - self.normalized_distance(source, target, cost)

if(__name__ == '__main__'):
    print("hermetrics is similar but different")
    