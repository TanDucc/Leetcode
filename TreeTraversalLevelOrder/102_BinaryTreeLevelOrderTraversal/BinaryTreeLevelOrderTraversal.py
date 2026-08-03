from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    res = []
    q = deque()
    q.append(root)
    
    while q:
        qLen = len(q)
        level = []
        for i in range(qLen):
            node = q.popleft()
            if node:
                level.append(node.val)
                q.append(node.left)
                q.append(node.right)
        if level:
            res.append(level)
    return res

# Example usage:

# Constructing a binary tree:
#       3
#      / \          
#     9  20
#        /  \   
#       15   7
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(levelOrder(root))  # Output: [[3], [9, 20], [15, 7]]
