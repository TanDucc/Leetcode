from typing import List

def findMaximumXOR(nums: List[int]) -> int:
    mask = 0
    res = 0
    
    for i in range(31, -1, -1):
        mask = mask | (1 << i)
        found = set([n & mask for n in nums])
        temp = res | (1 << i)
        
        for f in found:
            if (temp ^ f) in found:
                res = temp
                break
    return res

# Example usage:
nums = [3, 10, 5, 25, 2, 8]
print(findMaximumXOR(nums))  # Output: 28