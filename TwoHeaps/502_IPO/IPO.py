import heapq
from typing import List

def findMaximizedCapital(k: int, w: int, profits: List[int], capital: List[int]) -> int:
    maxProfit = []
    minCapital = [(c, p) for c, p in zip(capital, profits)]
    heapq.heapify(minCapital)
    
    for i in range(k):
        while minCapital and minCapital[0][0] <= w:
            c, p = heapq.heappop(minCapital)
            heapq.heappush(maxProfit,-1 * p)
        if not maxProfit:
            break
        w += -1 * heapq.heappop(maxProfit)
    return w

# Example usage:
k = 2
w = 0
profits = [1,2,3]
capital = [0,1,1]
result = findMaximizedCapital(k, w, profits, capital)
print(result)  # Output: 4