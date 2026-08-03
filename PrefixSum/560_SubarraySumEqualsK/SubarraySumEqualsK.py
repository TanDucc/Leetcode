from typing import List

def subarraySum(nums: List[int], k: int) -> int:
    res = 0
    curSum = 0
    prefixSums = {0 : 1}
    for n in nums:
        curSum += n
        diff = curSum - k
        res += prefixSums.get(diff, 0)
        prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)
    return res

nums = [1, 1, 1]
k = 2
result = subarraySum(nums, k)
print(result)  # Output: 2    