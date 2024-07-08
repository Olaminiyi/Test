import unittest
from solution1 import Solution  # Ensure this line correctly imports Solution from solution.py

class TestMaxProfit(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        self.assertEqual(self.solution.maxProfit([7, 1, 5, 3, 6, 4]), 5)

    def test_no_profit(self):
        self.assertEqual(self.solution.maxProfit([7, 6, 4, 3, 1]), 0)

    def test_single_day(self):
        self.assertEqual(self.solution.maxProfit([5]), 0)

    def test_empty_list(self):
        self.assertEqual(self.solution.maxProfit([]), 0)

    def test_increasing_prices(self):
        self.assertEqual(self.solution.maxProfit([1, 2, 3, 4, 5]), 4)

    def test_decreasing_then_increasing(self):
        self.assertEqual(self.solution.maxProfit([9, 7, 4, 1, 2, 5, 10]), 9)

    def test_large_input(self):
        prices = list(range(1000000, 0, -1))  # Large decreasing input
        self.assertEqual(self.solution.maxProfit(prices), 0)

if __name__ == '__main__':
    unittest.main()
