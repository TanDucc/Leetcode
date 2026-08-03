from typing import Optional

class TreeNode:
    def __init__(self, val: int = 0, left: 'Optional[TreeNode]' = None, right: 'Optional[TreeNode]' = None):
        self.val = val
        self.left = left
        self.right = right
def isSameTree(p: 'Optional[TreeNode]', q: 'Optional[TreeNode]') -> bool:
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False
    
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)