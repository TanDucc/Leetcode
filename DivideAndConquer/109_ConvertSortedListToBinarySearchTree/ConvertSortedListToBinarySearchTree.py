class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        n = 0
        cur = head
        
        while cur:
            cur = cur.next
            n += 1
        self.head = head
            
        def helper(l, r):
            if l > r:
                return None
            
            mid = (l + r) // 2
            left = helper(l, mid - 1)
            
            root = TreeNode(head.val)
            head = head.next
            root.left = left
            root.right = helper(mid + 1, r)
            return root
            
        return helper(0, n - 1)