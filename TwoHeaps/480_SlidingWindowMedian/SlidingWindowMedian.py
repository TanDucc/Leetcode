from typing import List
from sortedcontainers import SortedList

def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        list = SortedList()
        res = []
        
        for i in range(len(nums)):
            list.add(nums[i])
            if i >= k:
                list.remove(nums[i - k])
            if i >= k - 1:
                if k % 2 == 0:
                    median = (list[k // 2 - 1] + list[k // 2]) / 2
                else:
                    median = list[k // 2]
                res.append(median)
        return res
    
# Example usage:
nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(medianSlidingWindow(None, nums, k)) #[1, -1, -1, 3, 5, 6]