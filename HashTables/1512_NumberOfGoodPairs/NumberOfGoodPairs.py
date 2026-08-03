from typing import List

def numIdenticalPairs(self, nums: List[int]) -> int:
    res = 0
    count = {}
    for n in nums:
        if n in count:
            res += count[n]
            count[n] += 1
        else:
            count[n] = 1
    return res

# Example usage:
nums = [1, 2, 3, 1, 1, 3]
solution = numIdenticalPairs(None, nums)  # Passing None for self since it's not a class method
print(solution)  # Output: 4
        
#def numIdenticalPairs(self, nums: List[int]) -> int:
#    res = 0   
#    count = Counter(nums)
#    for n, c in count.items():
#        res += c * (c - 1) // 2
#    return res         