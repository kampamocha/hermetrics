import unittest

from hermetrics import MetricComparator

class TestMetricComparator(unittest.TestCase):
    
    def test_similarity(self):
        """
        Test for similarity function
        """
        m = MetricComparator()
        expected = {'Hamming': 0.5,
                    'Levenshtein': 0.5,
                    'OSA': 0.5,
                    'Damerau-Levenshtein': 0.5,
                    'Jaccard': 0.4,
                    'Dice': 0.571,
                    'Jaro': 0.722,
                    'Jaro-Winkler': 0.722}
        obtained = m.similarity("hardin", "martinez")
        for k, v in obtained.items():
            self.assertAlmostEqual(v, expected[k], places=3)
               
if __name__ == '__main__':
    unittest.main()