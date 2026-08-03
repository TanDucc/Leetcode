class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def minDiffInBST(root: TreeNode) -> int:
    prev, res = None, float('inf')
    
    def dfs(node):
        if not node:
            return
        nonlocal prev, res
        
        dfs(node.left)
        if prev:
            res = min(res, node.val - prev.val)
        prev = node
        dfs(node.right)
        
    dfs(root)
    return res

# Example usage:
# Constructing a simple BST:
#       4
#      / \
#     2   6
#    / \
#   1   3
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
print(minDiffInBST(root))  # Output: 1
