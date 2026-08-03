class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0, head)      # Tạo node giả để dễ thao tác đầu danh sách
        groupPrev = dummy              # Con trỏ trỏ đến node trước nhóm hiện tại

        while True:
            kth = self.getKthNode(groupPrev, k)  # Tìm node thứ k kể từ groupPrev
            if not kth:                          # Nếu không đủ k node thì dừng
                break
            groupNext = kth.next                 # Node sau nhóm đảo

            # Đảo ngược nhóm k node
            prev, cur = kth.next, groupPrev.next
            while cur != groupNext:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp

            # Nối lại nhóm đã đảo vào danh sách
            temp = groupPrev.next        # temp là node đầu nhóm trước khi đảo
            groupPrev.next = kth         # Nối node trước nhóm với node cuối nhóm (sau khi đảo)
            groupPrev = temp             # Di chuyển groupPrev đến cuối nhóm vừa đảo

        return dummy.next                # Trả về đầu danh sách mới

    def getKthNode(self, curr: ListNode, k: int) -> ListNode:
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr                      # Trả về node thứ k kể từ curr, hoặc None nếu không đủ k node