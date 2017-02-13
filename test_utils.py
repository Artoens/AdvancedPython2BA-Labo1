# test_utils.py
# Author: Sébastien Combéfis
# Version: February 2, 2016

import unittest
import utils

#coucou

class TestUtils(unittest.TestCase):
    class TestUtils(unittest.TestCase):
        def test_fact(self):
            self.assertEqual(utils.fact(0), 1)
            self.assertEqual(utils.fact(1), 1)
            self.assertEqual(utils.fact(3), 6)

        def test_roots(self):
            self.assertEqual(utils.root(0, 0, 0), ())
            self.assertEqual(utils.root(1, 2, 1), (1))
            self.assertEqual(utils.root(1, 0, -1), (1, -1) or (-1, 1))

        def test_integrate(self):
            self.assertEqual(utils.integrate(1, 0, 1), (1))
            pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())