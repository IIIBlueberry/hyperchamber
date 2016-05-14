import unittest
import tensorflow as tf
import numpy as np

import hyperchamber as hc


class hyperchamber_test(unittest.TestCase):
    def test_set(self):
        hc.reset()
        hc.set('x', [1])
        self.assertEqual(hc.configs(1), [{'x':1}])

    def test_set2(self):
        hc.reset()
        hc.set('x', [1,2])
        self.assertEqual(hc.configs(2), [{'x':1},{'x':2}])


    def test_configs(self):
        hc.reset()
        self.assertEqual(hc.configs(), [])

    def test_reset(self):
        hc.reset()
        self.assertEqual(hc.configs(), [])

if __name__ == '__main__':
    unittest.main()
