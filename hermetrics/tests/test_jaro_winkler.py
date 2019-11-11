# NOTE:
# For now the tests only check functionality with costs = 1
# Use other costs at your own peril

import unittest

from hermetrics.jaro_winkler import JaroWinkler

class TestJaroWinkler(unittest.TestCase):
    
    def test_distance(self):
        """
        Test for distance function
        """
        m = JaroWinkler()
        self.assertEqual(m.distance("abc", "abc"), 0)
        self.assertEqual(m.distance("abc", "def"), 1)
        self.assertEqual(m.distance("abc", ""), 1)
        self.assertEqual(m.distance("", "abc"), 1)
        self.assertEqual(m.distance("", ""), 0)
        self.assertEqual(m.distance("abcd", "dcba"), 0.5)  
        self.assertAlmostEqual(m.distance("abcd", "abe"), 0.222, places=3)
        self.assertAlmostEqual(m.distance("abcd", "abef"), 0.267, places=3)
        self.assertAlmostEqual(m.distance("abcde", "abcdx"), 0.080, places=3)
        self.assertAlmostEqual(m.distance("abcde", "axcde"), 0.120, places=3)        
        self.assertAlmostEqual(m.distance("abcd01234", "abcd56789", p=0.05), 0.296, places=3)
        self.assertAlmostEqual(m.distance("abcd01234", "abcd56789", p=0.15), 0.148, places=3)
        self.assertAlmostEqual(m.distance("abcd01234", "abcd56789", p=0.25), 0.0, places=3)
        self.assertAlmostEqual(m.distance(["hello","world"], ["hello","cruel","world"]), 0.350, places=3)

    def test_similarity(self):
        """
        Test for similarity function
        """
        m = JaroWinkler()
        self.assertEqual(m.similarity("abc", "abc"), 1)
        self.assertEqual(m.similarity("abc", "def"), 0)
        self.assertEqual(m.similarity("abc", ""), 0)
        self.assertEqual(m.similarity("", "xyz"), 0)
        self.assertEqual(m.similarity("", ""), 1)
        self.assertEqual(m.similarity("abcd", "dcba"), 0.5)        
        self.assertAlmostEqual(m.similarity("abcd", "abe"), 0.778, places=3)
        self.assertAlmostEqual(m.similarity("abcd", "abef"), 0.733, places=3)
        self.assertAlmostEqual(m.similarity("abcde", "abcdx"), 0.920, places=3)
        self.assertAlmostEqual(m.similarity("abcde", "axcde"), 0.880, places=3)        
        self.assertAlmostEqual(m.similarity("abcd01234", "abcd56789", p=0.05), 0.704, places=3)
        self.assertAlmostEqual(m.similarity("abcd01234", "abcd56789", p=0.15), 0.852, places=3)
        self.assertAlmostEqual(m.similarity("abcd01234", "abcd56789", p=0.25), 1.0, places=3)
        self.assertAlmostEqual(m.similarity(["hello","world"], ["hello","cruel","world"]), 0.650, places=3)
        
if __name__ == '__main__':
    unittest.main()