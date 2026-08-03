from typing import List
from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
    subtrees = defaultdict(list)
    res = []
    
    def dfs(node):
        if not node:
            return "null"
        s = ",".join([str(node.val), dfs(node.left), dfs(node.right)])
        if len(subtrees[s]) == 1:
            res.append(node)
        subtrees[s].append(node)
        return s
    dfs(root)
    return res
    