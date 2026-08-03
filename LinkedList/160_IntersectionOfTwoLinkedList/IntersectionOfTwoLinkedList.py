class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def getIntersectionNode(headA: ListNode, headB: ListNode):
    ListA, ListB = headA, headB
    while ListA != ListB:
        ListA = ListA.next if ListA else headB
        ListB = ListB.next if ListB else headA
    return ListA

