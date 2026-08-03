from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
def pathSum(root: TreeNode, targetSum: int) -> int:
    total = 0
    prefix = defaultdict(int)
    prefix[0] = 1  
    
    def dfs(node, curr_sum):
        nonlocal total
        if not node:
            return
        
        curr_sum += node.val
        total += prefix[curr_sum - targetSum]
        prefix[curr_sum] += 1
        
        dfs(node.left, curr_sum)
        dfs(node.right, curr_sum)
        
        prefix[curr_sum] -= 1
        
    dfs(root, 0)
    return total