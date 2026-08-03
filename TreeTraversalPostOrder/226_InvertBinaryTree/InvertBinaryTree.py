class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def invertTree(root):
    if not root:
        return None
    
    root.left, root.right = root.right, root.left
    invertTree(root.left)
    invertTree(root.right)
    return root

# Example usage:
# Construct a binary tree
#       4
#      / \
#     2   7
#    / \ / \
#   1  3 6  9
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)
# Invert the binary tree
inverted_root = invertTree(root)
# The inverted tree should be:
#       4
#      / \
#     7   2
#    / \ / \
#   9  6 3  1