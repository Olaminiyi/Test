
import unittest
from solution1 import Solution

class TestMaxSubArray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_single_element(self):
        self.assertEqual(self.solution.maxSubArray([1]), 1)
        self.assertEqual(self.solution.maxSubArray([-1]), -1)

    def test_multiple_elements(self):
        self.assertEqual(self.solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]), 6)
        self.assertEqual(self.solution.maxSubArray([1,2,3,4,5]), 15)
        self.assertEqual(self.solution.maxSubArray([-1,-2,-3,-4,-5]), -1)
        self.assertEqual(self.solution.maxSubArray([4,-1,2,1]), 6)
        self.assertEqual(self.solution.maxSubArray([-2, -1]), -1)

    def test_mixed_elements(self):
        self.assertEqual(self.solution.maxSubArray([3, -1, 2, -1]), 4)
        self.assertEqual(self.solution.maxSubArray([-2, -3, 4, -1, -2, 1, 5, -3]), 7)
        self.assertEqual(self.solution.maxSubArray([8, -19, 5, -4, 20]), 21)

if __name__ == '__main__':
    unittest.main()