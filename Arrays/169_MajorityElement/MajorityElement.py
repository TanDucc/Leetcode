from typing import List

def majorityElement(nums: List[int]) -> int:
    count, result = 0, 0
    for num in nums:
        if count == 0:
            result = num
        count += (1 if result == num else -1)
    return result             


nums = [2, 2, 1, 1, 1, 2, 2]
print(majorityElement(nums))  