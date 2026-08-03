from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val: int = 0, left: 'Optional[TreeNode]' = None, right: 'Optional[TreeNode]' = None):
        self.val = val
        self.left = left
        self.right = right
        
def widthOfBinaryTree(root: 'Optional[TreeNode]') -> int:
    res = 0
    prevLevel, prevNum = 0, 1
    q = deque([[root, 1, 0]])
    
    while q:
        node, num, level = q.popleft()
        if prevLevel < level:
            prevLevel = level
            prevNum = num
            
        res = max(res, num - prevNum + 1)
        if node.left:
            q.append([node.left, num * 2, level + 1])
        if node.right:
            q.append([node.right, num * 2 + 1, level + 1])
            
    return res

# Example usage:
# Constructing a binary tree:
#       1
#      / \
#     3   2
#    / \   \
#   5   3   9
root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(2)
root.left.left = TreeNode(5)
root.left.right = TreeNode(3)
root.right.right = TreeNode(9)
print(widthOfBinaryTree(root))  # Output: 4