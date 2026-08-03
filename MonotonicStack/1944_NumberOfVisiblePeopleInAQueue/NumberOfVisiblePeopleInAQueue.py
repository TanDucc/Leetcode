from typing import List

def canSeePersonsCount(self, heights: List[int]) -> List[int]:
    stack = []
    res = [0] * len(heights)
    
    for i in range(len(heights) - 1, -1, -1):
        h = heights[i]
        visible = 0
        
        while stack and stack[-1] < h:
            stack.pop()
            visible += 1
        if stack:
            visible += 1
        res[i] = visible
        stack.append(h)
    return res

# Example usage:
heights = [10, 6, 8, 5, 11, 9]
result = canSeePersonsCount(None, heights)
print(result)  # Output: [3, 1, 2, 1, 1, 0]