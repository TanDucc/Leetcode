class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    self.res = None
    
    def dfs(node):
        if not node:
            return False
        left = dfs(node.left)
        right = dfs(node.right)
        cur = node == p or node == q
        if (left and right) or (cur and (left or right)):
            self.res = node
            return
        return left or right or cur
    dfs(root)
    return self.res