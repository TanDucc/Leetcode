from typing import List

def rotate(self, nums: List[int],k: int) -> None:
    k = k % len(nums)
    left, right = 0, len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left, right = left + 1, right - 1
    left, right = 0, k - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left, right = left + 1, right - 1
    left, right = k, len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left, right = left + 1, right - 1
        
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotate(None, nums, k)
print(nums)         