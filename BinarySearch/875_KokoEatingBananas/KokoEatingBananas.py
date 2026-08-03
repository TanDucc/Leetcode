from typing import List
import math

def minEatingSpeed(piles: List[int], h: int) -> int:
    l, r = 1, max(piles)
    res = r
    
    while l <= r:
        k = (l + r) // 2
        hours = 0
        
        for p in piles:
            hours += math.ceil(p / k)
        if hours <= h:
            res = min(res, k)
            r = k - 1
        else:
            l = k + 1
    return res

piles = [3,6,7,11]
h = 8
print(minEatingSpeed(piles, h))  # Output: 4