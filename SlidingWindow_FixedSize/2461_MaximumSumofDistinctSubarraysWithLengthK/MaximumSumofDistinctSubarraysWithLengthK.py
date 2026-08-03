from typing import List

def maximumSumDistinctSubarrays(nums: List[int], k: int) -> int:
    curSum = 0
    prev_idx = {}
    res = 0
    l = 0
    for r in range(len(nums)):
        curSum += nums[r]
        i = prev_idx.get(nums[r], -1)
        while l <= i or r - l + 1 > k:
            curSum -= nums[l]
            l += 1
        if r - l + 1 == k:
            res = max(res, curSum)
        prev_idx[nums[r]] = r
    return res
# Example usage:
nums = [1, 2, 3, 2, 5]
k = 3
print(maximumSumDistinctSubarrays(nums, k)) 
    