import heapq
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        
    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
    
# Example usage:
kthLargest = KthLargest(3, [4, 5, 8, 2])
print(kthLargest.add(3))  # returns 4
print(kthLargest.add(5))  # returns 5
print(kthLargest.add(10)) # returns 5
print(kthLargest.add(9))  # returns 8
print(kthLargest.add(4))  # returns 8