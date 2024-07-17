
import unittest

from solution1 import Solution

class TestContainsDuplicate(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_contains_duplicate(self):
        self.assertTrue(self.solution.containsDuplicate([1, 2, 3, 1]), "Should return True for [1, 2, 3, 1]")
        self.assertFalse(self.solution.containsDuplicate([1, 2, 3, 4]), "Should return False for [1, 2, 3, 4]")
        self.assertTrue(self.solution.containsDuplicate([1, 1, 1, 1]), "Should return True for [1, 1, 1, 1]")
        self.assertFalse(self.solution.containsDuplicate([1]), "Should return False for [1]")
        self.assertFalse(self.solution.containsDuplicate([]), "Should return False for []")
        self.assertTrue(self.solution.containsDuplicate([1, 2, 3, 4, 2]), "Should return True for [1, 2, 3, 4, 2]")

if __name__ == '__main__':
    unittest.main()