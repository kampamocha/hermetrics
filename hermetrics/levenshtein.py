from matplotlib.pyplot import gca
from .metric import Metric

class Levenshtein(Metric):
    
    def __init__(self, name='Levenshtein'):
        super().__init__(name=name)
      
    def distance(self, source, target, cost=(1,1,1), show=False):
        """Levenshtein distance with costs for deletion, insertion and substitution"""
        s_len = len(source)
        t_len = len(target)  
    
        if type(cost) == int or type(cost) == float:
            del_cost = ins_cost = sub_cost = cost
        else:
            del_cost, ins_cost, sub_cost = cost
           
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
    
        if show:
            self.show_matrix(source, target, D)
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

    def show_matrix(self, source, target, M):
        """Show matrix with values from calculation"""       
        #ax = plt.gca()
        ax = gca()
        ax.set_yticks(range(len(source)+1))
        ax.set_xticks(range(len(target)+1))
        ax.set_yticklabels(list("ø" + source))
        ax.set_xticklabels(list("ø" + target))
        ax.tick_params(top=True, bottom=False, labeltop=True, labelbottom=False)
        
        for i in range(len(M)):
            for j in range(len(M[0])):
                ax.text(j, i, M[i][j], ha='center', va='center')
        
        ax.imshow(M, aspect='equal', cmap='Blues')

    
if(__name__ == '__main__'):
    print("Levenshtein distance")
