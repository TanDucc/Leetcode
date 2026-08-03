class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def countNodes(root: 'TreeNode') -> int:
    if not root: return 0
    
    def left_height(node):
        if not node:
            return 0
        return 1 + left_height(node.left)
    def right_height(node):
        if not node:
            return 0
        return 1 + right_height(node.right)
    
    l, r = left_height(root), right_height(root)
    
    if l > r:
        return 1 + countNodes(root.left) + countNodes(root.right)
    else:
        return (2 ** l) - 1  # 2^l - 1
    
# Example usage:
# Constructing a complete binary tree:
#        1
#       / \
#      2   3
#     / \  /
#    4  5 6
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
print(countNodes(root))  # Output: 6
