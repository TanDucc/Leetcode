from typing import List

def maxProduct(nums: List[int]) -> int:
    res = max(nums)
    curMax, curMin = 1, 1
    
    for n in nums:
        if n == 0:
            curMax, curMin = 1, 1
            continue
        
        temp = curMax * n
        curMax = max(curMin * n, temp, n)
        curMin = min(curMin * n, temp, n)
        
        res = max(res, curMax)
    return res

# Example usage:
nums = [2, 3, -2, 4]
result = maxProduct(nums)
print(result)  # Output: 6    