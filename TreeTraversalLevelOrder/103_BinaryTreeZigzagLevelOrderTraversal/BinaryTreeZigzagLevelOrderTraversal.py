from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def zigzagLevelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    res = []
    q = deque([root] if root else [])
    
    while q:
        level = []
        for i in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        if len(res) % 2 == 1:
            level.reverse()
        res.append(level)
    return res

# Example usage:
# Constructing a binary tree:
#       1   
#      / \
#     2   3
#    / \   \
#   4   5   6
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

print(zigzagLevelOrder(root))  # Output: [[1], [3, 2], [4, 5, 6]]

    