

import unittest
from solution2 import Solution 

class TestProductExceptSelf(unittest.TestCase):

    def test_product_except_self(self):
        solution = Solution()
        
        # Define test cases
        test_cases = [
            ([1, 2, 3, 4], [24, 12, 8, 6]),
            ([0, 1, 2, 3], [6, 0, 0, 0]),
            ([1, 2, 3, 0], [0, 0, 0, 6]),
            ([2, 3, 4, 5], [60, 40, 30, 24]),
            ([1, 1, 1, 1], [1, 1, 1, 1]),
        ]
        
        # Run tests
        for nums, expected in test_cases:
            with self.subTest(nums=nums, expected=expected):
                self.assertEqual(solution.productExceptSelf(nums), expected)

# Run the tests
if __name__ == '__main__':
    unittest.main()