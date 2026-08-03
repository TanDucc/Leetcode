from typing import List

def searchInsert(nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return l

# Example usage:
nums = [1,3,5,6]
target = 5
print(searchInsert(nums, target))  # Output: 2