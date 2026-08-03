def rangebitwiseAnd(left: int, right: int) -> int:
    i = 0
    while left != right:
        left = left >> 1
        right = right >> 1
        i += 1
    return left << i

# Example usage:
left = 5
right = 7
result = rangebitwiseAnd(left, right)
print(f"The bitwise AND of numbers from {left} to {right} is: {result}")