# Write two unittest test cases for the `subtract_divide()` function
# in `mymath.py`
#
# 1. Check for correct results by providing example input.
# 2. Check that a `CustomZeroDivisionError` gets raised correctly.

import unittest
import mymath
from mymath import CustomZeroDivsionError

class TestMyMath(unittest.TestCase):
    def test_subtract_divide(self):
        self.assertEqual(mymath.subtract_divide(0, 0, 0), 1)
    def text_zero_divison_error(self):
        self.assertRaises(CustomZeroDivsionError)
if __name__ == "__main__":
    unittest.main()
