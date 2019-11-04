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

from hermetrics.osa import Osa

class TestOsa(unittest.TestCase):
    
    def test_distance(self):
        """
        Test for distance function
        """
        m = Osa()
        self.assertEqual(m.distance("abc", "abc"), 0)
        self.assertEqual(m.distance("abc", "def"), 3)
        self.assertEqual(m.distance("abc", ""), 3)
        self.assertEqual(m.distance("", "abc"), 3)
        self.assertEqual(m.distance("", ""), 0)
        self.assertEqual(m.distance("abc", "ca"), 3)

    def test_normalized_distance(self):
        """
        Test for normalized distance function
        """
        m = Osa()
        self.assertEqual(m.normalized_distance("abc", "abc"), 0)
        self.assertEqual(m.normalized_distance("abc", "xyz"), 1)
        self.assertEqual(m.normalized_distance("abc", ""), 1)
        self.assertEqual(m.normalized_distance("", "xyz"), 1)
        self.assertEqual(m.normalized_distance("", ""), 0)
        self.assertEqual(m.normalized_distance("end", "ended"), 0.4)
        self.assertEqual(m.normalized_distance("ABCDEFGH", "AB*D*F*H"), 0.375)
        self.assertEqual(m.normalized_distance("abc", "ca"), 1)

    def test_similarity(self):
        """
        Test for similarity function
        """
        m = Osa()
        self.assertEqual(m.similarity("abc", "abc"), 1)
        self.assertEqual(m.similarity("abc", "def"), 0)
        self.assertEqual(m.similarity("abc", ""), 0)
        self.assertEqual(m.similarity("", "def"), 0)
        self.assertEqual(m.similarity("", ""), 1)
        self.assertEqual(m.similarity("end", "ended"), 0.6)
        self.assertEqual(m.similarity("ABCDEFGH", "AB*D*F*H"), 0.625)
        self.assertEqual(m.similarity("abc", "ca"), 0)        
        
if __name__ == '__main__':
    unittest.main()