from typing import List

def findPeakElement(nums: List[int]) -> int:
    l, r = 0, len(nums) - 1
    
    while l <= r:
        m = l + (r - l) // 2
        
        if m > 0 and nums[m] < nums[m - 1]:
            r = m - 1
        elif m < len(nums) - 1 and nums[m] < nums[m + 1]:
            l = m + 1
        else:
            return m


# Example usage:
nums = [1,2,1,3,5,6,4]
print(findPeakElement(nums))