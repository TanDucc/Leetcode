from typing import Optional
from collections import deque

class Node:
    def __init__(self, val: int = 0, left: 'Optional[Node]' = None, right: 'Optional[Node]' = None, next: 'Optional[Node]' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
        
def connect(root: 'Optional[Node]') -> 'Optional[Node]':
    if not root:
        return None
    q = deque([root])
    
    while q:
        qLen = len(q)
        for i in range(qLen):
            node = q.popleft()
            if i < qLen - 1:
                node.next = q[0]
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
                
    return root

# Example usage:
# Constructing a binary tree:
#       1
#      / \
#     2   3
#    / \   \
#   4   5   6
