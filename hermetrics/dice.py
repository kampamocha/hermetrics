from .jaccard import Jaccard

class Dice(Jaccard):
    
    def __init__(self, name='Dice'):
        super().__init__(name=name)
    
    def similarity(self, source, target, cost=1):
        """Dice similarity"""   
        if len(source) == 0 and len(target) == 0:
            return 1
        
        J = super().similarity(source, target, cost)
        return 2 * J / (1 + J)
    
    def distance(self, source, target, cost=1):
        """Dice distance"""
        return 1 - self.similarity(source, target, cost)

   
if(__name__ == '__main__'):
    print("Dice similarity")

