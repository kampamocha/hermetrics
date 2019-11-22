# NOTE:
# For now the tests only check functionality with costs = 1
# Use other costs at your own peril

import unittest

from hermetrics.damerau_levenshtein import DamerauLevenshtein

class TestDamerauLevenshtein(unittest.TestCase):

    def test_distance(self):
        """
        Test for distance function
        """
        m = DamerauLevenshtein()
        self.assertEqual(m.distance("abc", "abc"), 0)
        self.assertEqual(m.distance("abc", "def"), 3)
        self.assertEqual(m.distance("abc", ""), 3)
        self.assertEqual(m.distance("", "abc"), 3)
        self.assertEqual(m.distance("", ""), 0)
        self.assertEqual(m.distance("abcd", "cbad"), 2)
        self.assertEqual(m.distance("abc", "ca"), 2)

    def test_normalized_distance(self):
        """
        Test for normalized distance function
        """
        m = DamerauLevenshtein()
        self.assertEqual(m.normalized_distance("abc", "abc"), 0)
        self.assertEqual(m.normalized_distance("abc", "def"), 1)
        self.assertEqual(m.normalized_distance("abc", ""), 1)
        self.assertEqual(m.normalized_distance("", "def"), 1)
        self.assertEqual(m.normalized_distance("", ""), 0)
        self.assertEqual(m.normalized_distance("end", "ended"), 0.4)
        self.assertEqual(m.normalized_distance("ABCDEFGH", "AB*D*F*H"), 0.375)
        self.assertEqual(m.normalized_distance("abcd", "cbad"), 0.5)
        self.assertAlmostEqual(m.normalized_distance("abc", "ca"), 2/3)

    def test_similarity(self):
        """
        Test for similarity function
        """
        m = DamerauLevenshtein()
        self.assertEqual(m.similarity("abc", "abc"), 1)
        self.assertEqual(m.similarity("abc", "def"), 0)
        self.assertEqual(m.similarity("abc", ""), 0)
        self.assertEqual(m.similarity("", "def"), 0)
        self.assertEqual(m.similarity("", ""), 1)
        self.assertEqual(m.similarity("end", "ended"), 0.6)
        self.assertEqual(m.similarity("ABCDEFGH", "AB*D*F*H"), 0.625)
        self.assertEqual(m.similarity("abcd", "cbad"), 0.5)
        self.assertAlmostEqual(m.similarity("abc", "ca"), 1/3)

if __name__ == '__main__':
    unittest.main()