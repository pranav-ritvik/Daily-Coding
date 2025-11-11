# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        L1=0
        L2=0
        p = headA
        while p:
            p = p.next
            L1 += 1
        p = headB
        while p:
            p = p.next
            L2 += 1
        while L1>L2:
            headA = headA.next
            L1 -= 1
        while L2>L1:
            headB = headB.next
            L2-=1
        while headA != headB:
            headA = headA.next
            headB = headB.next
        return headA
