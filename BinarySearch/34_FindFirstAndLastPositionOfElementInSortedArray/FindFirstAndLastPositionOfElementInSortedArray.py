from typing import List

def searchRange(nums: List[int], target: int) -> List[int]:
    left = binarySearch(nums, target, True)
    right = binarySearch(nums, target, False)
    return [left, right]

def binarySearch(nums, target, leftBias):
        l, r = 0, len(nums) - 1
        i = -1
        
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                i = mid
                if leftBias:
                    r = mid - 1
                else:
                    l = mid + 1
        return i

# Example usage:
nums = [5,7,7,8,8,10]
target = 8
print(searchRange(nums, target))  # Output: [3, 4]