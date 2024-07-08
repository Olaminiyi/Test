import unittest
from solution1 import Solution  # Ensure this line correctly imports Solution from solution.py

class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        self.assertEqual(self.solution.twoSum([2, 7, 11, 15], 9), [0, 1])

    def test_multiple_pairs(self):
        self.assertEqual(self.solution.twoSum([1, 2, 3, 4, 5], 9), [3, 4])
        self.assertEqual(self.solution.twoSum([1, 2, 3, 4, 5], 5), [1, 2])

    def test_no_solution(self):
        self.assertEqual(self.solution.twoSum([1, 2, 3, 4, 5], 10), [])

    def test_negative_numbers(self):
        self.assertEqual(self.solution.twoSum([-1, -2, -3, -4, -5], -8), [2, 4])
        self.assertEqual(self.solution.twoSum([-1, -2, -3, -4, -5], -5), [1, 2])  # Updated expected output

    def test_zero_target(self):
        self.assertEqual(self.solution.twoSum([0, 4, 3, 0], 0), [0, 3])
        self.assertEqual(self.solution.twoSum([0, 1, 2, -3], -3), [0, 3])

    def test_single_element(self):
        self.assertEqual(self.solution.twoSum([1], 1), [])
    
    def test_empty_list(self):
        self.assertEqual(self.solution.twoSum([], 0), [])

if __name__ == '__main__':
    unittest.main()
