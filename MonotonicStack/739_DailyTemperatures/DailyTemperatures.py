from typing import List

def dailyTemperatures(temperatures: List[int]) -> List[int]:
    res = [0] * len(temperatures)
    stack = []
    
    for i, t in enumerate(temperatures):
        while stack and t > stack[-1][0]:
            stackTemp, stackIdx = stack.pop()
            res[stackIdx] = i - stackIdx
        stack.append([t,i])
    return res

temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
result = dailyTemperatures(temperatures)
print(result)  # Output: [1, 1, 4, 2, 1, 1, 0, 0]