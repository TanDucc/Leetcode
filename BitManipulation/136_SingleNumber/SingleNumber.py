from typing import List

def singleNumber(nums: List[int]) -> int:
    result = 0
    for n in nums:
        result = result ^ n
    return result

nums = [4, 1, 2, 1, 2]
result = singleNumber(nums)
print(result)