from typing import List

def maximumGap(nums: List[int]) -> int:
    n = len(nums)
    if n < 2:
        return 0
    res = 0
    nums.sort()
    
    for i in range(1, n):
        res = max(res, nums[i] - nums[i - 1])
    return res


# Example usage:
nums = [3, 6, 9, 1]
result = maximumGap(nums)
print(result)
    