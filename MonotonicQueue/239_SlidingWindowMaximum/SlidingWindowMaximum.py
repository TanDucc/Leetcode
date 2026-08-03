from typing import List
from collections import deque

def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    output = []
    l = r = 0
    q = deque()
    
    while r < len(nums):
        while q and q[-1] < nums[r]:
            q.pop()
        q.append(r)
        
        if l > q[0]:
            q.popleft()
            
        if (r + 1) >= k:
            output.append(nums[q[0]])
            l += 1
        r += 1
    return output

# Example usage:
nums = [1,3,-1,-3,5,3,6,7]
k = 3
result = maxSlidingWindow(nums, k)
print(result) 