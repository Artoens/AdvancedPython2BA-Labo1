# test_utils.py
# Author: Sébastien Combéfis
# Version: February 2, 2016

import unittest
import utils

class TestUtils(unittest.TestCase):
    def test_fact(self):
        self.assertEqual(utils.fact(0), 1)
        self.assertEqual(utils.fact(-1), ValueError)
        self.assertEqual(utils.fact(3), 6)
        self.assertEqual(utils.fact(""), ValueError)
        pass

    def test_roots(self):
        self.assertEqual(utils.roots(1, -4, 3), (1, 3))
        self.assertEqual(utils.roots(0, 4, -16), (4))
        pass

    def test_integrate(self):
        self.assertEqual(utils.integrate("x", 0, 0), (0))
        pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())