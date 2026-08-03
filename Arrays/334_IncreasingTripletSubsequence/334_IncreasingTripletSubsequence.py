from typing import List

def increasingTriplet(nums: List[int]) -> bool:
    first, second = float('inf'), float('inf')
    for num in nums:
        if num <= first:
            first = num
        elif num <= second:
            second = num
        else:
            return True
    return False

nums = [1, 2, 3, 4, 5]
print(increasingTriplet(nums))  # Output: True