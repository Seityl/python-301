import unittest
import unittest_function

class UnitTestFunction(unittest.TestCase):
    def test_text_sum(self):
        self.assertEqual(unittest_function.calculate(), 10)
    
if __name__ == "__main__":
    unittest.main()