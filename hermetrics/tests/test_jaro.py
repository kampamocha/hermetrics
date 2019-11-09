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

from hermetrics.jaro import Jaro

class TestJaro(unittest.TestCase):
    
    def test_distance(self):
        """
        Test for distance function
        """
        m = Jaro()
        self.assertEqual(m.distance("abc", "abc"), 0)
        self.assertEqual(m.distance("abc", "def"), 1)
        self.assertEqual(m.distance("abc", ""), 1)
        self.assertEqual(m.distance("", "abc"), 1)
        self.assertEqual(m.distance("", ""), 0)
        self.assertEqual(m.distance("abcd", "dcba"), 0.5)        
        self.assertAlmostEqual(m.distance("abcd", "abe"), 0.278, places=3)
        self.assertAlmostEqual(m.distance("abcd", "abef"), 1/3)
        self.assertAlmostEqual(m.distance("prada", "darpa"), 0.378, places=3)
        self.assertAlmostEqual(m.distance(["hello","world"], ["hello","cruel","world"]), 0.389, places=3)

    def test_similarity(self):
        """
        Test for similarity function
        """
        m = Jaro()
        self.assertEqual(m.similarity("abc", "abc"), 1)
        self.assertEqual(m.similarity("abc", "def"), 0)
        self.assertEqual(m.similarity("abc", ""), 0)
        self.assertEqual(m.similarity("", "xyz"), 0)
        self.assertEqual(m.similarity("", ""), 1)
        self.assertEqual(m.similarity("abcd", "dcba"), 0.5)        
        self.assertAlmostEqual(m.similarity("abcd", "abe"), 0.722, places=3)
        self.assertAlmostEqual(m.similarity("abcd", "abef"), 2/3)
        self.assertAlmostEqual(m.similarity("prada", "darpa"), 0.622, places=3)

        self.assertAlmostEqual(m.similarity(["hello","world"], ["hello","cruel","world"]), 0.611, places=3)
        
if __name__ == '__main__':
    unittest.main()