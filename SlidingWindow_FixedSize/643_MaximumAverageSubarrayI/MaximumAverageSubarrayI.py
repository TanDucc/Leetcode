from typing import List

def findMaxAverage(nums: List[int], k: int) -> float:
    n = len(nums)
    curSum = 0
    
    for i in range(k):
        curSum += nums[i]
        maxAvg = curSum / k
    for i in range(k, n):
        curSum += nums[i] - nums[i - k]
        avg = curSum / k
        maxAvg = max(maxAvg, avg)
    return maxAvg        

nums = [1, 12, -5, -6, 50, 3]
k = 4
result = findMaxAverage(nums, k)
print(result)  