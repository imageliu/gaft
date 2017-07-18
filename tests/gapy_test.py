#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' Module for all test in ga.py
'''

import unittest

from individual_test import IndividualTest
from population_test import PopulationTest

def suite():
    test_suite = unittest.TestSuite([
        unittest.TestLoader().loadTestsFromTestCase(IndividualTest),
        unittest.TestLoader().loadTestsFromTestCase(PopulationTest),
    ])

    return test_suite

if '__main__' == __name__:
    result = unittest.TextTestRunner(verbosity=2).run(suite())

    if result.errors or result.failures:
        raise ValueError('Get erros and failures')
