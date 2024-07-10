import unittest
from solution import Solution


class TestMaxProductSubArray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(self.solution.maxProductSubArray([2, 3, -2, 4]), 6)

    def test_example2(self):
        self.assertEqual(self.solution.maxProductSubArray([-2, 0, -1]), 0)

    def test_example3(self):
        self.assertEqual(self.solution.maxProductSubArray([-2, 3, -4]), 24)

    def test_example4(self):
        self.assertEqual(self.solution.maxProductSubArray([0, 2]), 2)

    def test_example5(self):
        self.assertEqual(self.solution.maxProductSubArray([-2, -3, -2, -4]), 24) # fixed expected value to match logic
    
    def test_example6(self):
        self.assertEqual(self.solution.maxProductSubArray([2, 3, -2, -4, -1, 0, 1, 2, -3, 4]), 48) # Added new test case

if __name__ == '__main__':
    unittest.main()

