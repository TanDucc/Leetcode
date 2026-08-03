import heapq
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution: 
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        
        for i, lst in enumerate(lists):
            if lst:
                heapq.heappush(heap, (lst.val, i, lst))
                
        dummy = ListNode()
        cur = dummy
        count = len(lists)
        
        while heap:
            val, idx, node = heapq.heappop(heap)
            cur.next = node
            cur = cur.next
            
            if node.next:
                heapq.heappush(heap, (node.next.val, idx, node.next))
                count += 1
        return dummy.next
    
lists = [[1,4,5], [1,3,4], [2,6]] #res = [1,1,2,3,4,4,5,6]

