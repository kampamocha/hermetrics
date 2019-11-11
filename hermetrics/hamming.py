from .metric import Metric

# https://en.wikipedia.org/wiki/Hamming_distance
# In this version is not mandatory to have same length strings
class Hamming(Metric):
    
    def __init__(self, name='Hamming'):
        super().__init__(name=name)
    
    def distance(self, source, target, cost=1):
        """Hamming distance with right padding"""
        # Difference in length
        length_difference = abs(len(source) - len(target))
        dist = sum(s != t for s, t in zip(source, target))
        return  (length_difference + dist) * cost

    def max_distance(self, source, target, cost=1):
        """Hamming maximum distance value"""
        return max(len(source), len(target)) * cost

    
if(__name__ == '__main__'):
    print("Hamming distance")
