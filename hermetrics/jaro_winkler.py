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
