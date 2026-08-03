from typing import List

def longestOnes(nums: List[int], k: int) -> int:
    l, maxLength = 0, 0
    numZeroes = 0
    
    for r in range(len(nums)):
        if nums[r] == 0:
            numZeroes += 1
        while numZeroes > k:
            if nums[l] == 0:
                numZeroes -= 1
            l += 1
        maxLength = max(maxLength, r - l + 1)
    return maxLength

# Example usage:
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
result = longestOnes(nums, k)
print(result)  # Output: 6    