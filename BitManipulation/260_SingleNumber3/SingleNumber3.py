from typing import List

def singleNumber(nums: List[int]) -> List[int]:
    xor = 0
    for n in nums:
        xor ^= n
    diff_bit = 1
    while not (xor & diff_bit):
        diff_bit <<= 1
    a, b = 0, 0
    for n in nums:
        if n & diff_bit:
            a ^= n
        else:
            b ^= n
    return [a, b]

# Example usage:
nums = [1, 2, 1, 3, 2, 5]
result = singleNumber(nums)
print(result)  # Output: [3, 5] or [5, 3] depending on the order            