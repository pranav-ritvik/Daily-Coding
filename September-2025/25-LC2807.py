# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current and current.next:
            new = ListNode(math.gcd(current.val , current.next.val))
            new.next = current.next
            current.next = new
            current = new.next
        return head
