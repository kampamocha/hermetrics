from .hamming import Hamming
from .levenshtein import Levenshtein
from .osa import Osa
from .damerau_levenshtein import DamerauLevenshtein
from .jaccard import Jaccard
from .dice import Dice
from .jaro import Jaro
from .jaro_winkler import JaroWinkler

class MetricComparator:
    """Class for metric comparison"""

    def __init__(self, metrics=[ 
            Hamming(),
            Levenshtein(),
            Osa(),
            DamerauLevenshtein(),
            Jaccard(),
            Dice(),
            Jaro(),
            JaroWinkler() ]):
        """Class constructor - receives a list of metrics for computation"""
        self.metrics = metrics

    def __repr__(self):
        """Class representation"""
        return f'MetricComparator({self.source!r}-{self.target!r})'

    def similarity(self, source, target):
        """Method to compare similarity for two strings with various metrics"""
        results = { m.name: m.similarity(source, target) for m in self.metrics }
        return results


if(__name__ == '__main__'):  
    print("Metric comparator")

    
        
            