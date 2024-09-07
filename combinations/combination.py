import itertools

def find_combinations(nums, target):
    result = []
    for r in range(2, len(nums) + 1):
        for combo in itertools.combinations(nums, r):
            if sum(combo) == target:
                result.append(list(combo))
    return result

# Test the function
nums = [1, 3, 4, 5, 6, 8]
target = 8
combinations = find_combinations(nums, target)
print(combinations)
