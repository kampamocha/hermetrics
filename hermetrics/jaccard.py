from .metric import Metric

class Jaccard(Metric):
    
    def __init__(self, name='Jaccard'):
        super().__init__(name=name)

    def similarity(self, source, target, cost=1):
        """Jaccard similarity"""
        if len(source) == 0 and len(target) == 0:
            return 1
        s = set(source)
        t = set(target)
        return len(set.intersection(s, t)) / len(set.union(s, t))
    
    def distance(self, source, target, cost=1):
        """Jaccard distance"""
        return 1 - self.similarity(source, target, cost)
   
if(__name__ == '__main__'):
    print("Jaccard similarity")
