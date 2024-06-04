# Write a unittest test suite with at least two methods that test
# the functionality of the built-in `math` module.

import unittest
import math

class Testmath(unittest.TestCase):
    def test_floor_rounds_down(self):
        self.assertEqual(math.floor(3.4), 3)
    def test_square_root(self):
        self.assertEqual(math.sqrt(25), 5)
    def test_factorial(self):
        self.assertEqual(math.factorial(1), 2)

if __name__ == "__main__":
    unittest.main()
