class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def distributeCoins(self, root: TreeNode) -> int:
    self.res = 0
    
    def dfs(cur):
        if not cur:
            return 0
        leftExtra = dfs(cur.left)
        rightExtra = dfs(cur.right)
        coinsExtra = cur.val - 1 + leftExtra + rightExtra
        res += abs(coinsExtra)
        return coinsExtra
    dfs(root)
    return self.res