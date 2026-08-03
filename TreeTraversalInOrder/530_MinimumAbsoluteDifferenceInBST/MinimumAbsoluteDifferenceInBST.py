class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def getMinimumDifference(root: TreeNode) -> int:
    prev, res = None, float('inf')
    
    def inorder(node):
        nonlocal prev, res
        if not node:
            return
        inorder(node.left)
        if prev:
            res = min(res, node.val - prev.val)
        prev = node
        inorder(node.right)
    
    inorder(root)
    return res