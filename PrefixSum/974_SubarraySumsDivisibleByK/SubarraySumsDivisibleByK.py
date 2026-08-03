from typing import List
from collections import defaultdict

def subarraysDivByK(self, nums: List[int], k: int) -> int:
    res = 0
    prefix_sum = 0
    prefix_cnt = defaultdict(int)
    prefix_cnt[0] = 1
    
    for n in nums:
        prefix_sum += n
        remain = prefix_sum % k
        res += prefix_cnt[remain]
        prefix_cnt[remain] += 1
    return res

# Example usage
nums = [4, 5, 0, -2, -3, 1]
k = 5
result = subarraysDivByK(None, nums, k)
print(result)  # Output: 7    