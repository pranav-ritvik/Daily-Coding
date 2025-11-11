# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        little = head
        big = head
        while big and big.next:
            little = little.next
            big = big.next.next
            if little == big:
                return True
        return False
