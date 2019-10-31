#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 12:41:58 2019
Tests
@author: kampamocha
"""

# python3 -m unittest discover hermetrics/tests

# Check examples at:
# https://stackoverflow.com/questions/20258800/is-jellyfishs-damerau-levenshtein-distance-calculation-buggy
# https://thetaiko.wordpress.com/2011/01/21/damerau-levenshtein-distance-in-python/
# http://alias-i.com/lingpipe/demos/tutorial/stringCompare/read-me.html

# https://asecuritysite.com/forensics/simstring?word=loans%20and%20accounts%24loans%20accounts

import unittest

from hermetrics.metric import Metric

class TestMetric(unittest.TestCase):
    
    def test_distance(self):
        """
        Test for distance function
        """
        m = Metric()
        self.assertEqual(m.distance("abc", "abc"), 0)
        self.assertEqual(m.distance("abc", "def"), 1)
        self.assertEqual(m.distance("abc", ""), 1)
        self.assertEqual(m.distance("", "abc"), 1)
        self.assertEqual(m.distance("", ""), 0)

    def test_max_distance(self):
        """
        Test for max_distance function
        """
        m = Metric()
        self.assertEqual(m.max_distance("abc", "abc"), 1)
        self.assertEqual(m.max_distance("abc", "def"), 1)
        self.assertEqual(m.max_distance("abc", ""), 1)
        self.assertEqual(m.max_distance("", "abc"), 1)
        self.assertEqual(m.max_distance("", ""), 0)

    def test_min_distance(self):
        """
        Test for min_distance function
        """
        m = Metric()
        self.assertEqual(m.min_distance("abc", "abc"), 0)
        self.assertEqual(m.min_distance("abc", "def"), 0)
        self.assertEqual(m.min_distance("abc", ""), 0)
        self.assertEqual(m.min_distance("", "abc"), 0)
        self.assertEqual(m.min_distance("", ""), 0)

    def test_normalize(self):
        """
        Test for normalization function
        """
        m = Metric()
        self.assertEqual(m.normalize(0, 0, 1), 0)
        self.assertEqual(m.normalize(1, 0, 1), 1)
        self.assertEqual(m.normalize(0.5, 0, 1), 0.5)
        self.assertEqual(m.normalize(0, 0, 20), 0)
        self.assertEqual(m.normalize(20, 0, 20), 1)
        self.assertEqual(m.normalize(8, 0, 20), 0.4)
        self.assertEqual(m.normalize(12, 10, 20), 0.2)
        self.assertEqual(m.normalize(8, 10, 20), 0)
        self.assertEqual(m.normalize(24, 10, 20), 1)
        self.assertEqual(m.normalize(0, -1, 1), 0.5)        
        self.assertEqual(m.normalize(0, 0, 0), 0)
        self.assertEqual(m.normalize(1, 1, 1), 0)
        self.assertEqual(m.normalize(50, 100, 1), 0)

    def test_normalized_distance(self):
        """
        Test for normalized distance function
        """
        m = Metric()
        self.assertEqual(m.normalized_distance("abc", "abc"), 0)
        self.assertEqual(m.normalized_distance("abc", "def"), 1)
        self.assertEqual(m.normalized_distance("abc", ""), 1)
        self.assertEqual(m.normalized_distance("", "abc"), 1)
        self.assertEqual(m.normalized_distance("", ""), 0)

    def test_similarity(self):
        """
        Test for similarity function
        """
        m = Metric()
        self.assertEqual(m.similarity("abc", "abc"), 1)
        self.assertEqual(m.similarity("abc", "def"), 0)
        self.assertEqual(m.similarity("abc", ""), 0)
        self.assertEqual(m.similarity("", "abc"), 0)
        self.assertEqual(m.similarity("", ""), 1)
        
if __name__ == '__main__':
    unittest.main()