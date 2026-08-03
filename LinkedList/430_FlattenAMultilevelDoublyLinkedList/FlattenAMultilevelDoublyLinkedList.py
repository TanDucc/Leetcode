class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head
        
        dummy = Node(0)
        cur, stack = dummy, [head]
        
        while stack:
            temp = stack.pop()
            if temp.next:
                stack.append(temp.next)
            if temp.child:
                stack.append(temp.child)
            cur.next = temp
            temp.prev = cur
            temp.child = None
            cur = temp
        dummy.next.prev = None
        return dummy.next