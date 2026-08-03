from typing import List

def search(nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        if nums[l] <= nums[mid]:  # Left side is sorted
            if target > nums[mid] or target < nums[l]: # Target is not in the left side
                l = mid + 1
            else:  # Target is in the left side
                r = mid - 1
        else:  # Right side is sorted
            if target < nums[mid] or target > nums[r]:  # Target is not in the right side
                r = mid - 1
            else:  # Target is in the right side
                l = mid + 1
    return -1

# Example usage:
nums = [4,5,6,0,1,2,3]
target = 5
print(search(nums, target)) 