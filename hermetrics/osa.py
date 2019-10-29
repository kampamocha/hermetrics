#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 09:22:59 2019
Optimal String Alignment distance
@author: kampamocha
"""
# https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance
# Optimal String Alignment (OSA) also known as Restrited Edit distance is a 
# simpler version of the Damerau-Levenshtein (DL) distance having the condiiton
# that no substring is edited more than once, whereas the DL distance presents
# no such restriction
from hermetrics.levenshtein import Levenshtein

class Osa(Levenshtein):
    
    def __init__(self, name='OSA'):
        super().__init__(name=name)

    def distance(self, source, target, cost=(1, 1, 1, 1), show=False):
        """OSA (Optimal String Alignment) distance with costs for deletion, insertion, substitution and transposition"""
        s_len = len(source)
        t_len = len(target)  
    
        if type(cost) == int or type(cost) == float:
            del_cost = ins_cost = sub_cost = tra_cost = cost
        else:
            del_cost, ins_cost, sub_cost, tra_cost = cost
        
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
                substitution_or_not = D[i-1][j-1]
                if source[i-1] != target[j-1]:
                    substitution_or_not += sub_cost
                    
                D[i][j] = min(deletion, insertion, substitution_or_not)
                
                if i > 1 and j > 1 and source[i-1] == target[j-2] and source[i-2] == target[j-1]:
                    D[i][j] = min(D[i][j], D[i-2][j-2] + tra_cost)
        
        if show:
            self.show_matrix(source, target, D)
        return D[-1][-1]  
    

    def max_distance_with_transpositions(self, source, target, cost=(1,1,1,1)):
        """
        OSA maximum distance value.
        This version does consider transpositions, but used with the
        normalization function supress the effect of them
        
        """
        s_len = len(source)
        t_len = len(target)
    
        if type(cost) == int or type(cost) == float:
            del_cost = ins_cost = sub_cost = tra_cost = cost
        else:
            del_cost, ins_cost, sub_cost, tra_cost = cost
        # Adjust substitution and transposition costs
        sub_cost = min(sub_cost, del_cost + ins_cost)
        tra_cost = min(tra_cost, sub_cost * 2)
        # Calc maximum number of operations
        max_del = max(s_len - t_len, 0)
        max_ins = max(t_len - s_len, 0)
        max_sub = min(s_len, t_len)
        max_tra = int(max_sub / 2)
        extra_sub = max_sub % 2
        # Calc max distances per operation type
        del_dist = max_del * del_cost
        ins_dist = max_ins * ins_cost
        sub_dist = max_sub * sub_cost
        tra_dist = max_tra * tra_cost + extra_sub * sub_cost
           
        return del_dist + ins_dist + min(sub_dist, tra_dist)
