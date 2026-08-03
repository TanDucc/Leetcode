from typing import List 

def minSubarrayLen(target: int, nums: List[int]) -> int:
    l, total = 0, 0
    res = float("inf")
    
    for r in range(len(nums)):
        total += nums[r]
        while total >= target:
            res = min(res, r - l + 1)
            total -= nums[l]
            l += 1
    return 0 if res == float("inf") else res

# Example usage:
target = 7
nums = [2, 3, 1, 2, 4, 3]
result = minSubarrayLen(target, nums)
print(result)  