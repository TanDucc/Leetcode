from typing import List

def subsets(nums: List[int]) -> List[List[int]]:
    res = []
    subset = []
    
    def dfs(i):
        if i >= len(nums):
            res.append(subset.copy())
            return
        
        # Decision to include nums[i]
        subset.append(nums[i])
        dfs(i + 1)
        
        # Decision NOT to include nums[i]
        subset.pop()
        dfs(i + 1)
    dfs(0)
    return res

# Example usage:
nums = [1, 2, 3]
print(subsets(nums))
