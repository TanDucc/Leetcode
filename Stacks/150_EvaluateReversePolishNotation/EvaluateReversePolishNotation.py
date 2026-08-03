from typing import List

def evalRPN(tokens: List[str]) -> int:
    stack = []
    
    for c in tokens:
        if c == "+":
            stack.append(stack.pop() + stack.pop())
        elif c == "-":
            a, b = stack.pop(), stack.pop()
            stack.append(b - a)
        elif c == "*":
            stack.append(stack.pop() * stack.pop())
        elif c == "/":
            a, b = stack.pop(), stack.pop()
            stack.append(int(b / a))
        else:
            stack.append(int(c))
            
    return stack[0]

# Example usage:
tokens = ["2","1","+","3","*"]
result = evalRPN(tokens)
print(result)  # Output: 9