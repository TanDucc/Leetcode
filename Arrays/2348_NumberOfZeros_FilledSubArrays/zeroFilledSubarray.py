from typing import List

def zeroFilledSubarray(nums: List[int]) -> int:
    result, count = 0, 0
    for i in range(len(nums)):
        if nums[i] == 0:
            count += 1
            result += count
        else:
            count = 0
    return result        

nums = [1, 3, 0, 0, 2, 0, 0, 4]
print(zeroFilledSubarray(nums))  # Output: 6            