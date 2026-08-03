from typing import List

#def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
#    index_map = {}
#    for i, num in enumerate(nums):
#        if num in index_map and i - index_map[num] <= k:
#            return True
#        index_map[num] = i
#    return False

def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    window = set()
    L = 0
    for R in range(len(nums)):
        if R - L > k:
            window.remove(nums[L])
            L += 1
        if nums[R] in window:
            return True
        window.add(nums[R])
    return False

# Example usage:
nums = [1, 2, 3, 1]
k = 3
result = containsNearbyDuplicate(nums, k)
print(result)  # Output: True        
    