class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def diameterOfBinaryTree(self, root: TreeNode) -> int:
    self.res = 0
    
    def dfs(cur):
        if not cur:
            return 0
        left = dfs(cur.left)
        right = dfs(cur.right)
        self.res = max(self.res, left + right)
        return max(left, right) + 1
    
    dfs(root)
    return self.res

# Example usage:
# Construct a binary tree
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
# Calculate the diameter of the binary tree
diameter = diameterOfBinaryTree(None, root)
