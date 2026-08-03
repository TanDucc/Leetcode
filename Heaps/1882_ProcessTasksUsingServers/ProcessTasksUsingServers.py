import heapq
from typing import List

def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
    res = [0] * len(tasks)
    available = [(servers[i], i) for i in range(len(servers))]
    heapq.heapify(available)
    unavail = []
    t = 0
    
    for i in range(len(tasks)):
        t = max(t, i)
        
        if len(available) == 0:
            t = unavail[0][0]
        while unavail and unavail[0][0] <= t:
            freetime, weight, index = heapq.heappop(unavail)
            heapq.heappush(available, (weight, index))
        weight, index = heapq.heappop(available)
        res[i] = index
        heapq.heappush(unavail, (t + tasks[i], weight, index))
    return res

# Example usage:
servers = [3,3,2]
tasks = [1,2,3,2,1,2]
result = assignTasks(None, servers, tasks)
print(result)  # Output: [2,2,0,2,1,2]
    