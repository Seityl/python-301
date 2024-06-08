# Write a script that demonstrates TDD. Using pseudocode, plan out
# a couple of small functions. They could be as fundamental as adding
# and subtracting numbers with each other,
# or more complex such as functions that read and write to files.
#
# Instead of writing the functions, however, only write the tests for them.
# Think about how your functions might fail and write tests that will check 
# for that and identify these failures.
#
# You do not need to implement the actual functions after writing the tests 
# but of course you can do that, too.

import math
import unittest

class Test(unittest.TestCase):
    def test_add(self):
        self.assertEqual(self + self)
    def test_multiply(self):
        self.assertEqual(self * self)

if __name__ == "__main__":
    unittest.main()