#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 18:27:43 2019
Levenshtein distance
@author: kampamocha
"""
from hermetrics.metric import Metric

class Levenshtein(Metric):
    
    def __init__(self, name='Levenshtein'):
        super().__init__(name=name)
      
    def distance(self, source, target, cost=(1,1,1)):
        """Levenshtein distance with costs for deletion, insertion and substitution"""
        s_len = len(source)
        t_len = len(target)  
    
        if type(cost) == int or type(cost) == float:
            del_cost = ins_cost = sub_cost = cost
        else:
            del_cost, ins_cost, sub_cost = cost
        
        if s_len == 0:
            return t_len * ins_cost
        if t_len == 0:
            return s_len * del_cost
    
        rows = s_len + 1
        cols = t_len + 1
        D = [[0 for j in range(cols)] for i in range(rows)]
    
        # source prefixes can be transformed into empty strings 
        # by deletions:
        for i in range(1, rows):
            D[i][0] = i * del_cost
        # target prefixes can be created from an empty source string
        # by inserting the characters
        for j in range(1, cols):
            D[0][j] = j * ins_cost
            
        for j in range(1, cols):
            for i in range(1, rows):
                deletion = D[i-1][j] + del_cost
                insertion = D[i][j-1] + ins_cost
                substitution_or_equal = D[i-1][j-1]
                if source[i-1] != target[j-1]:
                    substitution_or_equal += sub_cost
                          
                D[i][j] = min(deletion, insertion, substitution_or_equal)
    
        return D[-1][-1]
        
    def max_distance(self, source, target, cost=(1,1,1)):
        """Levenshtein maximum distance value"""
        s_len = len(source)
        t_len = len(target)
    
        if type(cost) == int or type(cost) == float:
            del_cost = ins_cost = sub_cost = cost
        else:
            del_cost, ins_cost, sub_cost = cost
    
        max_del = max(s_len - t_len, 0)
        max_ins = max(t_len - s_len, 0)
        max_sub = min(s_len, t_len)
        
        return max_del*del_cost + max_ins*ins_cost + max_sub*sub_cost
    
if(__name__ == '__main__'):
    print("Levenshtein distance")

