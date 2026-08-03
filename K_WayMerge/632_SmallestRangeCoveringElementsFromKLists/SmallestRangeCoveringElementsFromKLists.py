from typing import List
import heapq

def smallestRange(nums: List[List[int]]) -> List[int]:
    k = len(nums)
    left = right = nums[0][0]
    minHeap = []
    
    for i in range(k):
        l = nums[i]
        left = min(left, l[0])
        right = max(right, l[0])
        heapq.heappush(minHeap, (l[0], i, 0)) #value, list_idx, idx_value
    
    res = [left, right]
    
    while True:
        value, lst, idx = heapq.heappop(minHeap)
        idx += 1
        
        if idx == len(nums[lst]):
            return res
        nextValue = nums[lst][idx]
        heapq.heappush(minHeap, (nextValue, lst, idx))
        left = minHeap[0][0]
        right = max(right, nextValue)
        
        if right - left < res[1] - res[0]:
            res = [left, right]
        
    
# Example usage:
nums = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
print(smallestRange(nums))  # Output: [20,24]