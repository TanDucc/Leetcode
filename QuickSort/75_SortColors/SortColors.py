from typing import List

def sortColors(nums: List[int]) -> None:
    l, r = 0, len(nums) - 1
    i = 0
    
    while i <= r:
        if nums[i] == 0:
            nums[i], nums[l] = nums[l], nums[i]
            l += 1
            i += 1
        elif nums[i] == 2:
            nums[i], nums[r] = nums[r], nums[i]
            r -= 1
        else:
            i += 1
            
# Example usage:
nums = [2, 0, 2, 1, 1, 0]
sortColors(nums)
print(nums)  # Output: [0, 0, 1, 1, 2, 2]