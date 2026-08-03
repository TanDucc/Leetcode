from typing import List
import heapq

def maxEvents(events: List[List[int]]) -> int:
    events.sort()
    min_heap = []
    res = 0
    i = 0
    n = len(events)
    
    for day in range(1, 100001):
        while i < n and events[i][0] == day:
            heapq.heappush(min_heap, events[i][1])
            i += 1
        
        while min_heap and min_heap[0] < day:
            heapq.heappop(min_heap)
        
        if min_heap:
            heapq.heappop(min_heap)
            res += 1
        
        if i >= n and not min_heap:
            break
    return res

events = [[1,2],[2,3],[3,4]]
print(maxEvents(events))

