from typing import List

def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    res = []
    candidates.sort()  # Sort to handle duplicates
    
    def dfs(i, cur, total):
        if total == target:
            res.append(cur.copy())
            return
        if i == len(candidates) or total > target:
            return
        # Decision to include candidates[i]
        cur.append(candidates[i])
        dfs(i + 1, cur, total + candidates[i])
        # Decision NOT to include candidates[i]
        cur.pop()
        while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
            i += 1  # Skip duplicates
        dfs(i + 1, cur, total)
    dfs(0, [], 0)
    return res

# Example usage:
candidates = [10,1,2,7,6,1,5]
target = 8
print(combinationSum2(candidates, target))       
    