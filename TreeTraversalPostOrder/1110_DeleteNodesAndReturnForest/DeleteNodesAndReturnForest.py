class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def delNodes(root: TreeNode, to_delete: list[int]) -> list[TreeNode]:
    to_delete = set(to_delete)
    res_set = set([root])
    
    def dfs(node):
        if not node:
            return None
        res = node
        if node.val in to_delete:
            res = None
            res_set.discard(node)
            if node.left: 
                res_set.add(node.left)
            if node.right:
                res_set.add(node.right)
        node.left = dfs(node.left)
        node.right = dfs(node.right)
        return res
    dfs(root)
    return list(res_set)

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
root.right.right = TreeNode(6)
root.right.left = TreeNode(7)

# Nodes to delete
to_delete = [3, 5]
# Delete nodes and return the forest
forest = delNodes(root, to_delete)
# forest now contains the roots of the resulting trees after deletion
print([tree.val for tree in forest])  # Output the values of the roots in the forest

