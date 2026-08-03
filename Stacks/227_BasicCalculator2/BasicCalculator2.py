def calculate(s: str) -> int:
    stack = []
    cur, operator = 0, '+'
    allOperator = {'+', '-', '*', '/'}
    nums = set(str(x) for x in range(10))
    
    for i in range(len(s)):
        char = s[i]
        if char in nums:
            cur = cur * 10 + int(char)
        if char in allOperator or i == len(s) - 1:
            if operator == '+':
                stack.append(cur)
            elif operator == '-':
                stack.append(-cur)
            elif operator == '*':
                stack[-1] = stack[-1] * cur
            elif operator == '/':
                stack[-1] = int(stack[-1] / cur)
            operator = char
            cur = 0
    return sum(stack)

# Example usage:
s = "3+2*2"
result = calculate(s)
print(result)  # Output: 7        