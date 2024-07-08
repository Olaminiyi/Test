import unittest
from solution import Solution 

def test_groupAnagram():
    sol = Solution()
    
    # Test Case 1: General case
    input_strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    expected_output = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    assert sorted([sorted(group) for group in sol.groupAnagram(input_strs)]) == sorted([sorted(group) for group in expected_output])
    
    # Test Case 2: Single character strings
    input_strs = ["a", "b", "c", "a"]
    expected_output = [["a", "a"], ["b"], ["c"]]
    assert sorted([sorted(group) for group in sol.groupAnagram(input_strs)]) == sorted([sorted(group) for group in expected_output])
    
    # Test Case 3: Empty input list
    input_strs = []
    expected_output = []
    assert sol.groupAnagram(input_strs) == expected_output
    
    # Test Case 4: All anagrams
    input_strs = ["abc", "bca", "cab"]
    expected_output = [["abc", "bca", "cab"]]
    assert sorted([sorted(group) for group in sol.groupAnagram(input_strs)]) == sorted([sorted(group) for group in expected_output])
    
    # Test Case 5: No anagrams
    input_strs = ["abc", "def", "ghi"]
    expected_output = [["abc"], ["def"], ["ghi"]]
    assert sorted([sorted(group) for group in sol.groupAnagram(input_strs)]) == sorted([sorted(group) for group in expected_output])
    
    print("All test cases passed!")

# Run the test cases
test_groupAnagram()
