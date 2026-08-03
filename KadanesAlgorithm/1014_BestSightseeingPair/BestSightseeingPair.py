from typing import List

def maxScoreSightseeingPair(values: List[int]) -> int:
    res = 0
    curMax = values[0] - 1
    
    for i in range(1, len(values)):
        res = max(res, curMax + values[i])
        curMax = max(curMax - 1, values[i] - 1)
    return res

# Example usage:
values = [8, 1, 5, 2, 6]
result = maxScoreSightseeingPair(values)
print(result) 