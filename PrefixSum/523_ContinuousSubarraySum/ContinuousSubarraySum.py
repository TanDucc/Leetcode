from typing import List

def checkSubarraySum(nums: List[int], k: int) -> bool:
    remainder = {0 : -1}
    total = 0
    for i, n in enumerate(nums):
        total += n
        r = total % k
        if r not in remainder:
            remainder[r] = i
        elif i - remainder[r] > 1:
            return True
    return False

# Example usage
nums = [23, 2, 4, 6, 7]
k = 6
result = checkSubarraySum(nums, k)
print(result)  # Output: True     