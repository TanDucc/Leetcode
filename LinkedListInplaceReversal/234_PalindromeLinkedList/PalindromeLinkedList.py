class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast = head
        slow = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node
            
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
    
#Giả sử nửa sau đang là: 3 → 4 → 5 → None
#Ban đầu: prev = None, slow = 3

#Vòng 1:

#temp = 4
#slow.next = prev → 3.next = None
#prev = 3
#slow = 4

#Kết quả tạm: đoạn đã đảo 3 → None, còn lại 4 → 5 → None

#Vòng 2:

#temp = 5
#4.next = 3
#prev = 4
#slow = 5

#Kết quả tạm: đoạn đã đảo 4 → 3 → None, còn lại 5 → None

#Vòng 3:

#temp = None
#5.next = 4
#prev = 5
#slow = None (dừng vòng lặp)

#Kết quả cuối: prev = 5 → 4 → 3 → None

#Khi vòng lặp kết thúc, slow == None và prev chính là head của danh sách đã đảo.