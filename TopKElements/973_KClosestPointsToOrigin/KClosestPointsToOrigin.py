from typing import List
import heapq

def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    minHeap = []
    
    for (x, y) in points:
        distance = x * x + y * y
        minHeap.append([distance, x, y])
    heapq.heapify(minHeap)
    res = []
    
    while k > 0:
        distance, x, y = heapq.heappop(minHeap)
        res.append([x, y])
        k -= 1
    return res

points = [[1,3],[-2,2],[2,-2]]
k = 2
print(kClosest(points, k)) #[[-2,2],[2,-2]