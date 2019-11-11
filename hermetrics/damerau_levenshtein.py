from .levenshtein import Levenshtein

class DamerauLevenshtein(Levenshtein):
    
    def __init__(self, name='Damerau-Levenshtein'):
        super().__init__(name=name)

    def distance(self, source, target, cost=(1, 1, 1, 1), show=False):
        """Damerau-Levenshtein distance with costs for deletion, insertion, substitution and transposition"""
        s_len = len(source)
        t_len = len(target)  
    
        if type(cost) == int or type(cost) == float:
            del_cost = ins_cost = sub_cost = tra_cost = cost
        else:
            del_cost, ins_cost, sub_cost, tra_cost = cost
        
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
                                max((i-last_match_row-1) * del_cost, \
                                (j-last_match_col-1) * ins_cost) + tra_cost
                                
                D[i+1][j+1] = min(deletion, insertion, substitution, transposition)
                
                if opt_sub_cost == 0:
                    last_match_col = j
                    
            last_row[s_symbol] = i
        
        if show:
            self.show_matrix(source, target, [row[1:] for row in D[1:]])
        return D[-1][-1]
    
   
if(__name__ == '__main__'):
    print("Damerau-Levenshtein distance")
