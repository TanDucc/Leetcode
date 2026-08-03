from typing import List
import heapq

def kSmallestPairs(nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
    minHeap = []
    res = []
    
    for i in range(min(k, len(nums1))):
        heapq.heappush(minHeap, (nums1[i] + nums2[0], i, 0))
    
    while minHeap and len(res) < k:
        currentSum, i, j = heapq.heappop(minHeap)
        res.append([nums1[i], nums2[j]])
        
        if j + 1 < len(nums2):
            heapq.heappush(minHeap, (nums1[i] + nums2[j + 1], i, j + 1))
            
    return res

nums1 = [1,7,11]
nums2 = [2,4,6]
k = 3
print(kSmallestPairs(nums1, nums2, k))
