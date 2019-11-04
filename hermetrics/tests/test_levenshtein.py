#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 12:41:58 2019
Tests
@author: kampamocha
"""
# NOTE:
# For now the tests only check functionality with costs = 1
# Use other costs at your own peril

import unittest

from hermetrics.levenshtein import Levenshtein

class TestLevenshtein(unittest.TestCase):
    
    def test_distance(self):
        """
        Test for distance function
        """
        m = Levenshtein()
        self.assertEqual(m.distance("abc", "abc"), 0)
        self.assertEqual(m.distance("abc", "def"), 3)
        self.assertEqual(m.distance("abc", ""), 3)
        self.assertEqual(m.distance("", "abc"), 3)
        self.assertEqual(m.distance("", ""), 0)
        self.assertEqual(m.distance("start", "end"), 5)
        self.assertEqual(m.distance("end", "ended"), 2)
        self.assertEqual(m.distance("end", "weekend"), 4)
        self.assertEqual(m.distance("ABCDEFGH", "A*C*E*G*"), 4)
        self.assertEqual(m.distance("hello world", "helloworld"), 1)
        self.assertEqual(m.distance("survey", "surgery"), 2)

    def test_max_distance(self):
        """
        Test for max_distance function
        """
        m = Levenshtein()
        self.assertEqual(m.max_distance("abc", "abc"), 3)
        self.assertEqual(m.max_distance("abc", "xyz"), 3)
        self.assertEqual(m.max_distance("abc", ""), 3)
        self.assertEqual(m.max_distance("", "xyz"), 3)
        self.assertEqual(m.max_distance("", ""), 0)
        self.assertEqual(m.max_distance("start", "end"), 5)
        self.assertEqual(m.max_distance("end", "start"), 5)
        self.assertEqual(m.max_distance("ABCDEFGH", "A*C*E*G*"), 8)

    def test_normalized_distance(self):
        """
        Test for normalized distance function
        """
        m = Levenshtein()
        self.assertEqual(m.normalized_distance("abc", "abc"), 0)
        self.assertEqual(m.normalized_distance("abc", "xyz"), 1)
        self.assertEqual(m.normalized_distance("abc", ""), 1)
        self.assertEqual(m.normalized_distance("", "xyz"), 1)
        self.assertEqual(m.normalized_distance("", ""), 0)
        self.assertEqual(m.normalized_distance("start", "end"), 1)
        self.assertEqual(m.normalized_distance("end", "ended"), 0.4)
        self.assertEqual(m.normalized_distance("ABCDEFGH", "AB*D*F*H"), 0.375)

    def test_similarity(self):
        """
        Test for similarity function
        """
        m = Levenshtein()
        self.assertEqual(m.similarity("abc", "abc"), 1)
        self.assertEqual(m.similarity("abc", "def"), 0)
        self.assertEqual(m.similarity("abc", ""), 0)
        self.assertEqual(m.similarity("", "def"), 0)
        self.assertEqual(m.similarity("", ""), 1)
        self.assertEqual(m.similarity("start", "end"), 0)
        self.assertEqual(m.similarity("end", "ended"), 0.6)
        self.assertEqual(m.similarity("ABCDEFGH", "AB*D*F*H"), 0.625)
        
if __name__ == '__main__':
    unittest.main()