# NOTE:
# For now the tests only check functionality with costs = 1
# Use other costs at your own peril

import unittest

from hermetrics.jaccard import Jaccard

class TestJaccard(unittest.TestCase):
    
    def test_distance(self):
        """
        Test for distance function
        """
        m = Jaccard()
        self.assertEqual(m.distance("abc", "abc"), 0)
        self.assertEqual(m.distance("abc", "def"), 1)
        self.assertEqual(m.distance("abc", ""), 1)
        self.assertEqual(m.distance("", "abc"), 1)
        self.assertEqual(m.distance("", ""), 0)
        self.assertEqual(m.distance("abcd", "dcba"), 0)        
        self.assertEqual(m.distance("abcd", "abe"), 0.6)
        self.assertAlmostEqual(m.distance(["hello","world"], ["hello","cruel","world"]), 1/3)

    def test_similarity(self):
        """
        Test for similarity function
        """
        m = Jaccard()
        self.assertEqual(m.similarity("abc", "abc"), 1)
        self.assertEqual(m.similarity("abc", "def"), 0)
        self.assertEqual(m.similarity("abc", ""), 0)
        self.assertEqual(m.similarity("", "xyz"), 0)
        self.assertEqual(m.similarity("", ""), 1)
        self.assertEqual(m.similarity("abcd", "dcba"), 1)        
        self.assertEqual(m.similarity("abcd", "abe"), 0.4)
        self.assertAlmostEqual(m.similarity(["hello","world"], ["hello","cruel","world"]), 2/3)
        
if __name__ == '__main__':
    unittest.main()