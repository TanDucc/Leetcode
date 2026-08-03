from typing import List

def twoSum(numbers: List[int], target: int) -> List[int]:
    l, r = 0, len(numbers) - 1
    while l < r:
        curSum = numbers[l] + numbers[r]
        if curSum > target:
            r -= 1
        elif curSum < target:
            l += 1
        else:
            return [l + 1, r + 1]
    return []

# Example usage:
numbers = [2, 7, 11, 15]
target = 9
result = twoSum(numbers, target)
print(result)  # Output: [1, 2]        