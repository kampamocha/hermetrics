# NOTE:
# For now the tests only check functionality with costs = 1
# Use other costs at your own peril

import unittest

from hermetrics.dice import Dice

class TestDice(unittest.TestCase):
    
    def test_distance(self):
        """
        Test for distance function
        """
        m = Dice()
        self.assertEqual(m.distance("abc", "abc"), 0)
        self.assertEqual(m.distance("abc", "def"), 1)
        self.assertEqual(m.distance("abc", ""), 1)
        self.assertEqual(m.distance("", "abc"), 1)
        self.assertEqual(m.distance("", ""), 0)
        self.assertEqual(m.distance("abcd", "dcba"), 0)        
        self.assertAlmostEqual(m.distance("abcd", "abe"), 0.429, places=3)
        self.assertAlmostEqual(m.distance("abcd", "abef"), 0.5)
        self.assertAlmostEqual(m.distance(["hello","world"], ["hello","cruel","world"]), 0.2)

    def test_similarity(self):
        """
        Test for similarity function
        """
        m = Dice()
        self.assertEqual(m.similarity("abc", "abc"), 1)
        self.assertEqual(m.similarity("abc", "def"), 0)
        self.assertEqual(m.similarity("abc", ""), 0)
        self.assertEqual(m.similarity("", "xyz"), 0)
        self.assertEqual(m.similarity("", ""), 1)
        self.assertEqual(m.similarity("abcd", "dcba"), 1)        
        self.assertAlmostEqual(m.similarity("abcd", "abe"), 0.571, places=3)
        self.assertAlmostEqual(m.similarity("abcd", "abef"), 0.5)
        self.assertAlmostEqual(m.similarity(["hello","world"], ["hello","cruel","world"]), 0.8)
        
if __name__ == '__main__':
    unittest.main()