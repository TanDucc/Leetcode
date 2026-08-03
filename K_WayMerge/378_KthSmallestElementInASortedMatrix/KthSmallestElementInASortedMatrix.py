from typing import List
from bisect import bisect_right

def kthSmallest(matrix: List[List[int]], k: int) -> int:
    l, r, n = matrix[0][0], matrix[-1][-1], len(matrix)
    
    def lessK(m):
        count = 0 
        for row in range(n):
            x = bisect_right(matrix[row], m)
            count += x
        return count
    
    while l < r:
        mid = (l + r) // 2
        if lessK(mid) < k:
            l = mid + 1
        else:
            r = mid
    return l


matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8
print(kthSmallest(matrix, k))