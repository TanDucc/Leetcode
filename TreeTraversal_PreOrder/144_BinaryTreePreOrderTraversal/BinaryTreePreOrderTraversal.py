from typing import Optional, List
class TreeNode:
    def __init__(self, val: int = 0, left: 'Optional[TreeNode]' = None, right: 'Optional[TreeNode]' = None):
        self.val = val
        self.left = left
        self.right = right
        
def preorderTraversal(root: 'Optional[TreeNode]') -> List[int]:
    cur, stack, res = root, [], []
    
    while cur or stack:
        if cur:    
            res.append(cur.val)
            stack.append(cur.right)
            cur = cur.left
        else:
            cur = stack.pop()    
    return res

# Example usage:
# Constructing a binary tree:
#       1
#      / \
#     2   3
#    / \
#   4   5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print(preorderTraversal(root))  # Output: [1, 2, 4, 5, 3]