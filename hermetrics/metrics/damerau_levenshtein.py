#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 17:31:23 2019
Damerau-Levenshtein distance
@author: kampamocha
"""
# https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance
# G.V. Bard. Spelling-Error  Tolerant, Order-Independent Pass-Phrases via the Damerau-Lvenshtein String-Edit Distance Metric
# https://gist.github.com/badocelot/5327427
# Check optimization at https://web.archive.org/web/20150909134357/http://mwh.geek.nz:80/2009/04/26/python-damerau-levenshtein-distance/
from metrics.levenshtein import Levenshtein

class DamerauLevenshtein(Levenshtein):
    
    def __init__(self, name='Damerau-Levenshtein'):
        super().__init__(name=name)

    def distance(self, source, target, cost=(1, 1, 1, 1)):
        """Damerau-Levenshtein distance with costs for deletion, insertion, substitution and transposition"""
        s_len = len(source)
        t_len = len(target)  
    
        if type(cost) == int or type(cost) == float:
            del_cost = ins_cost = sub_cost = tra_cost = cost
        else:
            del_cost, ins_cost, sub_cost, tra_cost = cost
        
        if s_len == 0:
            return t_len * ins_cost
        if t_len == 0:
            return s_len * del_cost
       
        # Be sure to exceed maximum value
        #INF = float('inf')
        UPPER = max(del_cost, ins_cost, sub_cost, tra_cost) * (s_len + t_len)
    
        # Initialize matrix (s_len + 2) X (t_len + 2)
        D = [[UPPER for j in range(t_len + 2)]]
        D += [[UPPER] + [j*ins_cost for j in range(t_len + 1)]]
        D += [[UPPER, i] + [0]*t_len for i in range(1, s_len + 1)]
        
        # Holds last row each element was encountered
        last_row = {}
        
        for i in range(1, s_len + 1):
            # Current symbol in source
            s_symbol = source[i-1]
            # Column of lasta match on this row
            last_match_col = 0
            
            for j in range(1, t_len + 1):
                # Current symbol in target
                t_symbol = target[j-1]
                # Last row with matching character
                last_match_row = last_row.get(t_symbol, 0)
                # Cost of substitution
                opt_sub_cost = 0 if s_symbol == t_symbol else sub_cost
                
                # Compute different options
                deletion = D[i][j+1] + del_cost
                insertion = D[i+1][j] + ins_cost
                substitution = D[i][j] + opt_sub_cost
                # Cost before transposition
                # + cost of operations between transposed letters
                # + cost of transposition
    #            transposition = D[last_match_row][last_match_col] + \
    #                            (i-last_match_row-1) * del_cost + \
    #                            (j-last_match_col-1) * ins_cost + \
    #                            tra_cost
                transposition = D[last_match_row][last_match_col] + \
                                max((i-last_match_row-1) * del_cost, (j-last_match_col-1) * ins_cost) + \
                                tra_cost
                                
                D[i+1][j+1] = min(deletion, insertion, substitution, transposition)
                
                if opt_sub_cost == 0:
                    last_match_col = j
                    
            last_row[s_symbol] = i
        
        return D[-1][-1]
    
