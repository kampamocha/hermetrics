#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 15:27:52 2019
Python library for distance and similarity metrics
@author: kampamocha
"""
import hermetrics.metrics.hamming as hamming
import hermetrics.metrics.jaccard as jaccard
import hermetrics.metrics.jaro as jaro
import hermetrics.metrics.jaro_winkler as jaro_winkler
import hermetrics.metrics.levenshtein as levenshtein
import hermetrics.metrics.osa as osa
import hermetrics.metrics.damerau_levenshtein as damerau_levenshtein
import hermetrics.metrics.dice as dice

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
        #if high == low:
        #    return high
        if x >= high:
            return high
        if x <= low:
            return low
        return (x - low) / (high - low)
    
    def normalized_distance(self, source, target, cost=1):
        """Normalized distance between two objects"""
        return self.normalize(self.distance(source, target, cost), self.max_distance(source, target, cost), self.min_distance(source, target, cost))
    
    def similarity(self, source, target, cost=1):
        """Normalized similarity between two objects"""
        return 1 - self.normalized_distance(source, target, cost)

    # Class methods for initialization
    @classmethod
    def hamming(cls):
        name = 'Hamming'
        distance = hamming.distance
        max_distance = hamming.max_distance
        return cls(name=name, distance=distance, max_distance=max_distance)

    @classmethod
    def jaccard(cls):
        name = 'Jaccard'
        distance = jaccard.distance
        similarity = jaccard.similarity
        return cls(name=name, distance=distance, similarity=similarity)

    @classmethod
    def dice(cls):
        name = 'Dice'
        distance = dice.distance
        similarity = dice.similarity
        return cls(name=name, distance=distance, similarity=similarity)

    @classmethod
    def jaro(cls):
        name = 'Jaro'
        distance = jaro.distance
        similarity = jaro.similarity
        return cls(name=name, distance=distance, similarity=similarity)

    @classmethod
    def jaro_winkler(cls):
        name = 'Jaro-Winkler'
        distance = jaro_winkler.distance
        similarity = jaro_winkler.similarity
        return cls(name=name, distance=distance, similarity=similarity)

    @classmethod
    def levenshtein(cls):
        name = 'Levenshtein'
        distance = levenshtein.distance
        max_distance = levenshtein.max_distance
        return cls(name=name, distance=distance, max_distance=max_distance)

    @classmethod
    def osa(cls):
        name = 'OSA'
        distance = osa.distance
        max_distance = osa.max_distance
        return cls(name=name, distance=distance, max_distance=max_distance)

    @classmethod
    def damerau_levenshtein(cls):
        name = 'Damerau-Levenshtein'
        distance = damerau_levenshtein.distance
        max_distance = damerau_levenshtein.max_distance
        return cls(name=name, distance=distance, max_distance=max_distance)


if(__name__ == '__main__'):
    print("hermetrics is similar but different")
    