class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right  

def binaryTreePaths(root: 'TreeNode') -> list[str]:
    def dfs(node, path):
        if node:
            path += str(node.val)
            if not node.left and not node.right:
                res.append(path)
            else:
                path += "->"
                dfs(node.left, path)
                dfs(node.right, path)
    res = []
    dfs(root, "")
    return res

# Example usage:
# Constructing a binary tree:
#       1
#      / \
#     2   3
#      \
#       5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
print(binaryTreePaths(root))  # Output: ["1->2->5", "1->3"]